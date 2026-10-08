# DeepSeek Proxy Skill

A local OpenAI-compatible API proxy that turns your free DeepSeek web account into an API you can call from code.

## 🔒 Security Notice
**NEVER commit real DeepSeek tokens to this repository.** Each user must obtain their own token and add it to their local `.env` file.

## 📦 Installation

```bash
git clone https://github.com/javadhamed-ctrl/jj-skills.git
cd jj-skills/deepseek-proxy-skill

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium

# Get your DeepSeek token from https://chat.deepseek.com
# (Press F12 → Application → Local Storage → chat.deepseek.com → userToken)
# Add it to .env file (which is gitignored)

# Start the proxy
python proxy.py
```

## 📖 Usage

### With OpenCode
Select model `deepseek-local` in your OpenCode configuration.

### With Python
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

## 📁 Project Structure

```
deepseek-proxy-skill/
├── .env.example          # Placeholder - never commit real values!
├── .gitignore           # Ignores .env and session/
├── README.md            # This file
├── proxy.py             # Main proxy server
├── requirements.txt     # Python dependencies
├── setup.bat            # Windows setup wizard
└── SKILL.md             # ECC skill documentation
```

## ⚠️ Important

- **Token is personal**: Obtain your own from DeepSeek chat
- **Local only**: Proxy runs on `http://127.0.0.1:8000`
- **Never commit .env**: This file is gitignored for security
- **Responsibility**: Users own their token and DeepSeek ToS compliance

## 🛠️ Technical Details

- Built with FastAPI and uvicorn
- Uses playwright and curl_cffi to bypass Cloudflare
- OpenAI-compatible endpoint at `/v1/chat/completions`
- Lists models at `/v1/models`

## 📄 License

MIT License

## 🙏 Acknowledgements

- DeepSeek for their free chat service
- OpenAI for the API compatibility pattern