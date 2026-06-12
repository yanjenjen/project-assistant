@echo off
chcp 65001 >nul
cd /d "c:\Users\jenny.lu\Documents\艾創點數位-ERP顧問"

echo === 同步到 GitHub ===
echo.

git add -A

for /f "tokens=1-3 delims=/ " %%a in ("%date%") do set TODAY=%%a/%%b/%%c
for /f "tokens=1-2 delims=: " %%a in ("%time%") do set NOW=%%a:%%b

set MSG=更新 %TODAY% %NOW%

git commit -m "%MSG%"

if %errorlevel% == 0 (
    echo.
    echo 推送到 GitHub...
    git push
    echo.
    echo 同步完成！
) else (
    echo.
    echo 沒有新的變更需要同步。
)

echo.
pause
