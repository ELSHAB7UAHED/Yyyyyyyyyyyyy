@echo off
chcp 65001 >nul
cls

echo ========================================
echo   Ahmed SMS Tool - APK Builder
echo   Developer: Ahmed Nour
echo   Website: ahmednour.vercel.app
echo ========================================
echo.

REM Check if Docker is installed
docker --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Docker is not installed!
    echo.
    echo Please install Docker first:
    echo https://docs.docker.com/get-docker/
    pause
    exit /b 1
)

echo [INFO] Docker is installed
echo.

REM Build Docker image
echo [INFO] Building Docker image...
docker build -t ahmed-sms-builder .

if errorlevel 1 (
    echo [ERROR] Failed to build Docker image
    pause
    exit /b 1
)

REM Create directories
if not exist bin mkdir bin
if not exist .buildozer mkdir .buildozer

REM Run build
echo.
echo [INFO] Starting APK build process...
echo [INFO] This may take 20-40 minutes depending on your system...
echo.

docker run --rm ^
    -v "%CD%\bin:/app/bin" ^
    -v "%CD%\.buildozer:/app/.buildozer" ^
    ahmed-sms-builder ^
    buildozer -v android debug

if errorlevel 1 (
    echo.
    echo [ERROR] Build failed!
    pause
    exit /b 1
)

echo.
echo ========================================
echo [SUCCESS] Build completed!
echo ========================================
echo.

if exist bin\*.apk (
    echo APK files:
    dir /b bin\*.apk
    echo.
    echo To install on your device:
    echo   adb install bin\ahmedsmstool-*.apk
)

echo.
echo Developer: Ahmed Nour
echo Website: ahmednour.vercel.app
echo.
pause
