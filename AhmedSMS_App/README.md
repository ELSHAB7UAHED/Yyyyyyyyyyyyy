# Ahmed SMS Tool 🔐

## Professional Hacking Style Android Application

![Version](https://img.shields.io/badge/version-1.0.0-green)
![Platform](https://img.shields.io/badge/platform-Android-brightgreen)
![License](https://img.shields.io/badge/license-Educational-orange)

---

## 🎯 Features

- ✅ **Professional Hacking Style UI** - Matrix-inspired green theme with animations
- ✅ **Secure Login System** - Password verification with Telegram Bot integration
- ✅ **Dynamic Password Change** - Admin can change password via `pass=newpassword`
- ✅ **SMS Campaign Tool** - Send multiple SMS messages
- ✅ **Real-time Progress** - Live progress tracking with statistics
- ✅ **Activity Logging** - Complete log of all operations
- ✅ **Protected Numbers** - Immune numbers that cannot be targeted
- ✅ **Telegram Notifications** - Get notified of all activities

---

## 🔐 Security Features

### Password System
- Default password: `a`
- Change password: Type `pass=yournewpassword` in the password field
- All password changes are notified via Telegram Bot

### Protected Numbers
The following numbers are protected and cannot be targeted:
- `201014812328`
- `01014812328`

### Telegram Bot Integration
- **Bot Token**: `8124336394:AAFPPgpeg-0Gd-31BQMKfM4zKb7uM6crD64`
- **Admin Chat ID**: `201014812328`
- Notifications sent for:
  - Failed login attempts
  - Password changes
  - Attack completions

---

## 📱 Screenshots

The app includes 4 main screens:

1. **Login Screen** - Secure authentication with animated background
2. **Main Screen** - SMS campaign control center
3. **Settings Screen** - Password management and app info
4. **About Screen** - Developer information and disclaimer

---

## 🛠️ Building the APK

### Prerequisites

- Python 3.8+
- Buildozer
- Android SDK/NDK (auto-downloaded by buildozer)

### Installation

```bash
# Install buildozer
pip install buildozer

# Install dependencies
pip install -r requirements.txt
```

### Build Commands

```bash
# Build debug APK
python build.py

# Or use buildozer directly
buildozer -v android debug

# Build release APK
buildozer -v android release
```

### Output Location

After successful build:
```
./bin/ahmedsmstool-1.0.0-arm64-v8a_armeabi-v7a-debug.apk
```

---

## 📲 Installation

### Method 1: ADB
```bash
adb install ahmedsmstool-1.0.0-arm64-v8a_armeabi-v7a-debug.apk
```

### Method 2: Direct Install
1. Transfer APK to your Android device
2. Enable "Install from Unknown Sources" in Settings
3. Tap the APK file to install

---

## 🎨 UI Design

### Color Scheme
- **Primary**: Matrix Green (#00FF41)
- **Secondary**: Dark Green (#008F11)
- **Background**: Almost Black (#0A0A0A)
- **Surface**: Dark Gray (#1A1A1A)
- **Error**: Hacker Red (#FF0040)

### Animations
- Particle background effect
- Glowing text animations
- Smooth screen transitions
- Progress bar animations

---

## ⚠️ Disclaimer

**This tool is for EDUCATIONAL PURPOSES ONLY!**

- The developer is NOT responsible for any misuse
- Unauthorized use may violate local laws
- Only use on numbers you own or have permission to test

---

## 👨‍💻 Developer

**Ahmed Nour**
- 🌐 Website: [ahmednour.vercel.app](https://ahmednour.vercel.app)
- 📱 Telegram: @AhmedNourBot

---

## 📄 License

This project is for educational purposes only. Use at your own risk.

---

## 🙏 Credits

- Kivy Framework
- KivyMD Material Design
- Python Android Tools

---

**© 2024 Ahmed Nour - All Rights Reserved**
