# Installation Guide - Ahmed SMS Tool

## 🚀 Quick Start

Choose one of the following methods to build the APK:

### Method 1: Using Docker (Recommended) ⭐

#### Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/) (optional)

#### Linux/Mac
```bash
# Make build script executable
chmod +x build.sh

# Build using Docker
./build.sh docker
```

#### Windows
```batch
# Run the build script
build.bat
```

#### Using Docker Compose
```bash
docker-compose up --build
```

#### Using Docker directly
```bash
# Build the image
docker build -t ahmed-sms-builder .

# Create directories
mkdir -p bin .buildozer

# Run build
docker run --rm \
    -v "$(pwd)/bin:/app/bin" \
    -v "$(pwd)/.buildozer:/app/.buildozer" \
    ahmed-sms-builder \
    buildozer -v android debug
```

---

### Method 2: Local Build

#### Prerequisites

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install -y \
    python3 python3-pip python3-venv \
    git zip unzip openjdk-17-jdk \
    autoconf libtool pkg-config \
    zlib1g-dev libncurses5-dev \
    libncursesw5-dev libtinfo5 cmake \
    libffi-dev libssl-dev automake \
    gettext build-essential \
    libsqlite3-dev libjpeg-dev libpng-dev
```

**macOS:**
```bash
# Install Homebrew first: https://brew.sh/
brew install python git openssl autoconf automake libtool pkg-config
brew install --cask adoptopenjdk17
```

**Windows:**
1. Install [Python 3.8+](https://www.python.org/downloads/)
2. Install [Git](https://git-scm.com/download/win)
3. Install [JDK 17](https://adoptium.net/)
4. Install [Cygwin](https://www.cygwin.com/) or use WSL2

#### Build Steps

```bash
# Install buildozer and cython
pip3 install buildozer cython

# Navigate to project directory
cd AhmedSMS_App

# Build APK
./build.sh local
# OR
buildozer -v android debug
```

---

## 📱 Installing the APK

### Using ADB
```bash
# Connect your device via USB
# Enable USB debugging in Developer Options

# Install APK
adb install bin/ahmedsmstool-1.0.0-arm64-v8a_armeabi-v7a-debug.apk
```

### Direct Install
1. Transfer the APK file to your Android device
2. On device: Settings → Security → Enable "Unknown Sources"
3. Tap the APK file to install

---

## 🔧 Troubleshooting

### Build Errors

#### Error: "Cython not found"
```bash
pip3 install cython
```

#### Error: "Java compiler not found"
```bash
# Ubuntu/Debian
sudo apt-get install openjdk-17-jdk

# macOS
brew install --cask adoptopenjdk17
```

#### Error: "Permission denied"
```bash
# Make scripts executable
chmod +x build.sh
```

#### Error: "Out of memory"
```bash
# Increase Docker memory limit
# Or build locally instead
./build.sh local
```

### Docker Issues

#### Docker daemon not running
```bash
# Linux
sudo systemctl start docker

# macOS/Windows
# Start Docker Desktop application
```

#### Permission denied for Docker
```bash
# Linux - Add user to docker group
sudo usermod -aG docker $USER
# Log out and log back in
```

---

## 📋 Build Output

After successful build, the APK will be located at:
```
bin/ahmedsmstool-1.0.0-arm64-v8a_armeabi-v7a-debug.apk
```

---

## ⏱️ Build Time

- First build: 30-60 minutes (downloads SDK/NDK)
- Subsequent builds: 10-20 minutes

---

## 💡 Tips

1. **Use Docker** for consistent builds across different systems
2. **Keep the `.buildozer` folder** to speed up future builds
3. **Use SSD** for faster build times
4. **Stable internet connection** required for downloading dependencies

---

## 🆘 Support

For issues and questions:
- Website: [ahmednour.vercel.app](https://ahmednour.vercel.app)
- Telegram: @AhmedNourBot

---

**Developer: Ahmed Nour**  
**© 2024 All Rights Reserved**
