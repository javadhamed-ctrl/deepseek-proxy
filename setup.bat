@echo off
title DeepSeek Proxy Skill Setup
echo ==========================================
echo  DeepSeek Proxy Skill Setup
echo ==========================================
echo.
echo 1. Cloning repository...
echo.
git clone https://github.com/javadhamed-ctrl/jj-skills.git
cd jj-skills/deepseek-proxy-skill
echo.
echo 2. Installing Python dependencies...
echo.
pip install -r requirements.txt
echo.
echo 3. Installing Playwright browsers...
echo.
python -m playwright install chromium
echo.
echo 4. Setting up your DeepSeek token...
echo.
echo "   VERY IMPORTANT: You must get your own token from DeepSeek:"
echo "   1. Open https://chat.deepseek.com in your browser"
echo "   2. Press F12 to open DevTools"
echo "   3. Go to Application -> Local Storage -> chat.deepseek.com"
echo "   4. Find localStorage.getItem("userToken") and copy it"
echo "   5. Replace the value in .env below"
echo.
copy .env.example .env
notepad .env
echo.
echo 5. Starting proxy server...
echo.
python proxy.py > nul 2>&1 &
echo.
echo Proxy running at http://127.0.0.1:8000
echo.
echo 6. Testing proxy...
echo.
python -c "import requests; r = requests.get('http://127.0.0.1:8000/v1/models', timeout=5); print('Status:', r.status_code)"
echo.
echo ==========================================
echo  SETUP COMPLETE 
echo ==========================================
echo.
echo Important Reminders:
echo 1. Keep .env file LOCAL - never commit to GitHub
echo 2. Your token is personal - do not share it
echo 2. In OpenCode, select model: deepseek-local
echo 3. Proxy must be running to use with OpenCode
echo.
pause