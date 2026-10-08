# DeepSeek Proxy Skill

[فارسی](#فارسی) | [English](#english)

---

## فارسی

### 🔒 هشدار امنیتی
**هرگز توکن DeepSeek واقعی خود را در این ریپازیتوری commit نکنید.** هر کاربر باید توکن خودش را بگیرد و در فایل `.env` محلی‌اش قرار دهد.

### 📦 نصب

```bash
git clone https://github.com/javadhamed-ctrl/deepseek-proxy.git
cd deepseek-proxy

# نصب وابستگی‌ها
pip install -r requirements.txt

# نصب مرورگر Playwright
playwright install chromium

# دریافت توکن از https://chat.deepseek.com
# (F12 → Application → Local Storage → chat.deepseek.com → userToken)
# توکن را در فایل .env قرار دهید (این فایل gitignored است)

# شروع پراکسی
python proxy.py
```

### 📖 استفاده

**در OpenCode:**
مدل `deepseek-local` را انتخاب کنید.

**با Python:**
```python
from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:8000/v1",
    api_key="sk-live-your-token-here"
)

response = client.chat.completions.create(
    model="expert",
    messages=[{"role": "user", "content": "سلام!"}],
)
print(response.choices[0].message.content)
```

**با cURL:**
```bash
curl -X POST http://127.0.0.1:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-live-your-token-here" \
  -d '{"model": "expert", "messages": [{"role": "user", "content": "سلام!"}]}'
```

### 📁 ساختار پروژه

```
deepseek-proxy/
├── .env.example          # نمونه - هرگز مقادیر واقعی commit نکنید!
├── .gitignore           # نادیده گرفتن .env و session/
├── README.md            # این فایل
├── proxy.py             # سرور پراکسی اصلی
├── requirements.txt     # وابستگی‌های Python
├── setup.bat            # ویزارد نصب ویندوز
└── SKILL.md             # مستندات skill
```

### ⚠️ نکات مهم

- **توکن شخصی است**: هر کاربر باید توکن خودش را از DeepSeek بگیرد
- **فقط محلی**: پراکسی روی `http://127.0.0.1:8000` اجرا می‌شود
- **هرگز .env commit نکنید**: این فایل برای امنیت gitignored است
- **مسئولیت**: کاربران مسئول امنیت توکن و رعایت ToS DeepSeek هستند

---

## English

### 🔒 Security Notice
**NEVER commit real DeepSeek tokens to this repository.** Each user must obtain their own token and add it to their local `.env` file.

### 📦 Installation

```bash
git clone https://github.com/javadhamed-ctrl/deepseek-proxy.git
cd deepseek-proxy

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium

# Get your token from https://chat.deepseek.com
# (F12 → Application → Local Storage → chat.deepseek.com → userToken)
# Add it to .env file (which is gitignored)

# Start the proxy
python proxy.py
```

### 📖 Usage

**With OpenCode:**
Select model `deepseek-local`.

**With Python:**
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

**With cURL:**
```bash
curl -X POST http://127.0.0.1:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-live-your-token-here" \
  -d '{"model": "expert", "messages": [{"role": "user", "content": "Hello!"}]}'
```

### 📁 Project Structure

```
deepseek-proxy/
├── .env.example          # Placeholder - never commit real values!
├── .gitignore           # Ignores .env and session/
├── README.md            # This file
├── proxy.py             # Main proxy server
├── requirements.txt     # Python dependencies
├── setup.bat            # Windows setup wizard
└── SKILL.md             # Skill documentation
```

### ⚠️ Important

- **Token is personal**: Each user must obtain their own from DeepSeek
- **Local only**: Proxy runs on `http://127.0.0.1:8000`
- **Never commit .env**: This file is gitignored for security
- **Responsibility**: Users own their token security and DeepSeek ToS compliance

---

## 🛠️ Technical Details / جزئیات فنی

- Built with FastAPI and uvicorn / ساخته شده با FastAPI و uvicorn
- Uses playwright and curl_cffi to bypass Cloudflare / استفاده از playwright و curl_cffi برای دور زدن Cloudflare
- OpenAI-compatible endpoint at `/v1/chat/completions` / نقطه پایانی سازگار با OpenAI
- Lists models at `/v1/models` / لیست مدل‌ها در `/v1/models`

## 📄 License / مجوز

MIT License

## 🙏 Acknowledgements / تشکر

- DeepSeek for their free chat service / DeepSeek برای سرویس چت رایگانشان
- OpenAI for the API compatibility pattern / OpenAI برای الگوی سازگاری API
