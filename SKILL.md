# DeepSeek Proxy Skill

## Description
A local OpenAI-compatible API proxy that turns your free DeepSeek web account into an API you can call from code. Uses Playwright and curl_cffi to bypass Cloudflare and access DeepSeek's free chat interface.

## Prerequisites
- Python 3.9+
- A free DeepSeek account at chat.deepseek.com
- Playwright browsers installed (playwright install chromium)

## Installation

### 1. Clone the skill
```bash
git clone https://github.com/javadhamed-ctrl/jj-skills.git
cd jj-skills
```

### 2. Install dependencies
```bash
cd deepseek-proxy
pip install -r requirements.txt
```

### 3. Install Playwright browsers
```bash
playwright install chromium
```

### 3. Get your DeepSeek token
1. Open `https://chat.deepseek.com` in your browser
2. Press **F12** to open DevTools
3. Go to **Application** → **Local Storage** → `chat.deepseek.com`
4. Find `localStorage.getItem("userToken")`
5. Copy the entire value (starts with `eyJhbGci...`)

### 3. Configure the proxy
```bash
cp .env.example .env
# Edit .env and replace BELOW_TOKEN_HERE with your actual token
# DEEPSEEK_USER_TOKEN=eyJhbGciOiJ...your_actual_token_here...
```

### 4. Start the proxy
```bash
python proxy.py
```

The proxy will start at `http://127.0.0.1:8000`

## Usage

### With OpenCode
Add to your `opencode.jsonc` or `opencode.json`:
```json
{
  "model": "deepseek-local",
  "api_base": "http://127.0.0.1:8000/v1",
  "api_key": "sk-live-your-token-here",
  "parameters": {
    "temperature": 0.7,
    "max_tokens": 4096
  },
  "description": "DeepSeek Local Proxy",
  "enabled": true
}
```

### With Python (OpenAI-compatible)
```python
from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:8000/v1",
    api_key="sk-live-your-token-here"
)

response = client.chat.completions.create(
    model="expert",
    messages=[{"role": "user", "content": "Hello!"}],
)
print(response.choices[0].message.content)
```

### With cURL
```bash
curl -X POST http://127.0.0.1:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-live-your-token-here" \
  -d '{"model": "expert", "messages": [{"role": "user", "content": "Hello!"}]}'
```

## Configuration

### .env file
```
DEEPSEEK_USER_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJKdGF2YWRhdyIsImV4cGlyZWRfc3ViamVjdCI6ZmFsc2UsImlhdCI6MTc0NjgyOTA2MH0._example_sig
CF_CLEARANCE=your_cf_clearance_cookie_here
HOST=127.0.0.1
PORT=8000
DEFAULT_MODEL=expert
```

### OpenCode integration
The skill adds a `deepseek-local` provider to OpenCode's configuration. Users can select this model and use it just like any other OpenAI-compatible model.

## License
MIT License

## Important Notes
- **Token security**: Your DeepSeek user token gives access to your account - keep it secret
- **Rate limits**: Free tier has ~2 concurrent requests limit
- **Session refresh**: Sessions auto-refresh but may need re-login after extended inactivity
- **Terms of Use**: Using reverse proxies may violate DeepSeek's ToS - use at your own risk
- **Better alternative**: Consider official DeepSeek API for production use (paid tier)