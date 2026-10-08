# DeepSeek Proxy Skill

## Description
A local OpenAI-compatible API proxy that turns your free DeepSeek web account into an API you can call from code. Uses Playwright and curl_cffi to bypass Cloudflare and access DeepSeek's free chat interface.

⚠️ **IMPORTANT: This project requires each user to provide their own DeepSeek token. The token must NOT be committed to this repository.**

## Prerequisites
- Python 3.9+
- A free DeepSeek account at chat.deepseek.com
- Playwright browsers installed (playwright install chromium)

## 🔒 Token Security
**DO NOT commit your DeepSeek token to this repository.** Each user must obtain their own token and add it to their local `.env` file.

### How to Get Your Token
1. Open `https://chat.deepseek.com` in your browser
2. Press **F12** to open DevTools
3. Go to **Application** → **Local Storage** → `chat.deepseek.com`
4. Find `localStorage.getItem("userToken")`
5. Copy the entire value (starts with `eyJhbGci...`)
6. Add it to your local `.env` file - **DO NOT share this token or commit it to any repository**

## Installation

### 1. Clone the skill
```bash
git clone https://github.com/javadhamed-ctrl/jj-skills.git
cd jj-skills/deepseek-proxy-skill
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Install Playwright browsers
```bash
playwright install chromium
```

### 4. Set up your token
Copy `.env.example` to `.env`:
```bash
copy .env.example .env
```
Then edit `.env` and replace `DEEPSEEK_USER_TOKEN` with your actual token:
```bash
# Get your token first from https://chat.deepseek.com (F12 -> Application -> Local Storage -> userToken)
DEEPSEEK_USER_TOKEN=eyJhbGciOiJ...your_actual_token_here...
CF_CLEARANCE=
HOST=127.0.0.1
PORT=8000
DEFAULT_MODEL=expert
```

⚠️ **IMPORTANT: The `.env` file is gitignored and should NEVER be committed to GitHub. Real tokens must stay local.**

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

## Project Structure
```
deepseek-proxy-skill/
├── .env.example          # Placeholder - never commit real values!
├── .gitignore           # Ignores .env and session/
├── README.md            # This file (included in repo)
├── proxy.py             # Main proxy server
├── requirements.txt     # Python dependencies
├── setup.bat            # Windows setup wizard
└── SKILL.md             # This skill documentation
```

## License
MIT License

## Important Security Notes
- **Token personal**: Each user must obtain their own DeepSeek token
- **Never commit tokens**: Real tokens must never be added to this repository
- **Local only**: Proxy runs on `http://127.0.0.1:8000` (local only)
- **Responsibility**: Users are responsible for their own token security and DeepSeek ToS compliance
- **Support**: For issues, check the README or open an issue on GitHub

## Getting Help
- Check the `.env.example` for the expected format
- Ensure your token starts with `eyJhbGci...`
- Ensure the proxy is running before using OpenCode
- The proxy must be running in the background to use with OpenCode