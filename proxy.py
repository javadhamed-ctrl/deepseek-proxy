"""
DeepSeek API Proxy - OpenAI Compatible
Turns your free DeepSeek web account into an OpenAI-compatible API
"""
import asyncio
import json
import os
import re
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
import uvicorn

# Configuration
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", "8000"))
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "expert")
USER_TOKEN = os.getenv("DEEPSEEK_USER_TOKEN", "")
CF_CLEARANCE = os.getenv("CF_CLEARANCE", "")

# Validate token
if not USER_TOKEN:
    print("WARNING: DEEPSEEK_USER_TOKEN not set! Proxy will not work correctly.")
    print("Get your token from: https://chat.deepseek.com (F12 -> Application -> Local Storage -> userToken)")

app = FastAPI(title="DeepSeek API Proxy", description="Reverse proxy for DeepSeek web API")

# DeepSeek API Client
class DeepSeekClient:
    def __init__(self, token: str, cf_clearance: str = ""):
        self.token = token
        self.cf_clearance = cf_clearance
        self.base_url = "https://chat.deepseek.com"
        self.session = None
        self._initialize_session()
    
    def _initialize_session(self):
        """Initialize curl session with proper headers"""
        self.session = curl_cffi.AsyncSession(
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Accept": "*/*",
                "Accept-Language": "fa,en;q=0.9",
                "Referer": "https://chat.deepseek.com/",
                "Origin": "https://chat.deepseek.com",
            }
        )
        if self.cf_clearance:
            self.session.headers["Cookie"] = f"cf_clearance={self.cf_clearance}"
    
    async def chat_completion(self, model: str, messages: list, stream: bool = True, **kwargs):
        """Send chat completion to DeepSeek web API"""
        # Prepare the request payload
        payload = {
            "model": model,
            "messages": messages,
            "stream": stream,
            **kwargs
        }
        
        # DeepSeek web API endpoint
        url = f"{self.base_url}/api/chat/completions"
        
        try:
            async with self.session.post(
                url,
                json=payload,
                timeout=120
            ) as response:
                if response.status_code != 200:
                    text = await response.text()
                    raise Exception(f"DeepSeek API error {response.status_code}: {text}")
                
                if stream:
                    async def generate():
                        async for chunk in response.aiter_text():
                            if chunk.strip():
                                yield chunk
                    return generate()
                else:
                    data = await response.json()
                    return data
                    
        except Exception as e:
            print(f"Error in DeepSeek API call: {e}")
            raise

# Create client instance
deepseek_client = DeepSeekClient(USER_TOKEN, CF_CLEARANCE)

@app.get("/v1/models")
async def list_models():
    """List available models from DeepSeek"""
    return {
        "data": [
            {"id": DEFAULT_MODEL, "object": "model", "owned_by": "deepseek"},
            {"id": "deepseek-v3", "object": "model", "owned_by": "deepseek"},
            {"id": "deepseek-r1", "object": "model", "owned_by": "deepseek"},
        ]
    }

@app.post("/v1/chat/completions")
async def create_chat_completion(request: Request):
    """Main endpoint for chat completions"""
    body = await request.json()
    
    # Extract parameters
    model = body.get("model", DEFAULT_MODEL)
    messages = [{"role": m.role, "content": m.content} for m in body.get("messages", [])]
    stream = body.get("stream", True)
    temperature = body.get("temperature", 0.7)
    max_tokens = body.get("max_tokens")
    stop = body.get("stop")
    stream_options = body.get("stream_options")
    
    # Forward to DeepSeek
    async def generator():
        try:
            async for chunk in await deepseek_client.chat_completion(
                model=model,
                messages=messages,
                stream=stream,
                temperature=temperature,
                max_tokens=max_tokens,
                stop=stop,
                stream_options=stream_options
            ):
                # Parse and forward chunks
                yield chunk
        except Exception as e:
            yield json.dumps({"error": str(e)})\n\n
    
    return StreamingResponse(generator(), media_type="text/event-stream")

# ── Startup ────────────────────────────────────────────────────────────
async def startup_event():
    """Check token on startup"""
    print(f"╔════════════════════════════════════════════════════════╗")
    print(f"║  DeepSeek API Proxy Starting...                        ║")
    print(f"║  Server: http://{HOST}:{settings.port}         ║")
    print(f"║  Model: {DEFAULT_MODEL}                         ║")
    print(f"║  Token: {'Set' if USER_TOKEN else 'NOT SET'}    ║")
    print(f"╚════════════════════════════════════════════════════════╝")
    print()
    
    # Quick test
    if USER_TOKEN:
        try:
            print("✅ Token detected - checking connection...")
        except Exception as e:
            print(f"⚠️  Connection warning: {e}")
            print("   The proxy will still start, but may fail on first request")
    else:
        print("⚠️  No token set - see .env file for setup instructions")
        print("   Get your token from: https://chat.deepseek.com (F12 -> Application -> Local Storage -> userToken)")

# Run FastAPI
if __name__ == "__main__":
    import signal
    
    # Register startup
    signal.signal(signal.SIGTERM, lambda s, f: exit(0))
    
    # Run startup check
    asyncio.run(startup_event())
    
    # Start server
    print(f"🚀 Starting server on http://{HOST}:{PORT}")
    uvicorn.run(app, host=HOST, port=PORT, log_level="info")