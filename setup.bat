@echo off
title DeepSeek Proxy Skill Setup
echo ==========================================
echo  DeepSeek Proxy Skill Setup
echo ==========================================
echo.
echo 1. Installing Python dependencies...
echo.
cd /d "D:\Documents\Default Project\deepseek-proxy-skill"
python -m pip install -r requirements.txt >nul 2>&1
echo.
echo 2. Installing Playwright browsers...
echo.
python -m playwright install chromium >nul 2>&1
echo.
echo 3. Getting DeepSeek token...
echo.
echo "   Please get your token from: https://chat.deepseek.com"
echo "   (Press F12, go to Application -> Local Storage -> chat.deepseek.com)"
echo "   Then replace BELOW_TOKEN_HERE in .env"
echo.
echo 4. Starting proxy server...
echo.
python proxy.py > proxy.log 2>&1
echo.
echo Proxy running at http://127.0.0.1:8000
echo.
echo 5. Testing proxy...
echo.
python -c "import requests; r = requests.get('http://127.0.0.1:8000/v1/models', timeout=5); print('Status:', r.status_code)"
echo.
echo ==========================================
echo  SETUP COMPLETE 
echo ==========================================
echo.
echo Important: 
echo 1. Keep the proxy running for OpenCode to use it
echo 2. In OpenCode, select model: deepseek-local
echo 3. Get your token from: https://chat.deepseek.com
echo.
pause