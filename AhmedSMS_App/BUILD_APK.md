# كيفية بناء ملف APK - Ahmed SMS Tool

## 🚀 طرق بناء APK

### الطريقة 1: Google Colab (الأسهل والأسرع) ⭐

1. افتح الملف `Build_APK_on_Colab.ipynb` في Google Colab
2. شغل جميع الخلايا بالترتيب
3. انتظر 20-40 دقيقة
4. حمل ملف APK الناتج

**رابط Colab المباشر:**
```
https://colab.research.google.com/github/YOUR_USERNAME/AhmedSMS_App/blob/main/Build_APK_on_Colab.ipynb
```

---

### الطريقة 2: GitHub Actions (مجاني وآلي)

1. أنشئ مستودع GitHub جديد
2. ارفع جميع ملفات المشروع
3. اذهب إلى تبويب Actions
4. شغل workflow "Build APK"
5. انتظر 20-30 دقيقة
6. حمل APK من قسم Artifacts

**الملف المستخدم:** `.github/workflows/build-apk.yml`

---

### الطريقة 3: Termux (على الهاتف مباشرة)

1. ثبت Termux من F-Droid
2. شغل الأوامر التالية:

```bash
# تحديث الحزم
pkg update && pkg upgrade -y

# تثبيت المتطلبات
pkg install -y python git zip unzip openjdk-17 autoconf libtool pkg-config cmake libffi openssl automake gettext patchelf

# تثبيت buildozer
pip install buildozer cython

# نسخ المشروع
cd ~
mkdir -p AhmedSMS_App
cd AhmedSMS_App

# انسخ ملفات المشروع هنا (main.py, buildozer.spec)

# بناء APK
buildozer -v android debug

# بعد الانتهاء، انسخ APK إلى التخزين
cp bin/*.apk /sdcard/Download/
```

**أو استخدم السكريبت الجاهز:**
```bash
bash build-termux.sh
```

---

### الطريقة 4: Docker (للمستخدمين المتقدمين)

```bash
# بناء صورة Docker
docker build -t ahmed-sms-builder .

# تشغيل البناء
docker run --rm \
    -v "$(pwd)/bin:/app/bin" \
    -v "$(pwd)/.buildozer:/app/.buildozer" \
    ahmed-sms-builder \
    buildozer -v android debug
```

**أو استخدام Docker Compose:**
```bash
docker-compose up --build
```

---

### الطريقة 5: Linux/Mac المحلي

#### المتطلبات:
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y \
    python3-pip build-essential git zip unzip \
    openjdk-17-jdk autoconf libtool pkg-config \
    zlib1g-dev libncurses5-dev libncursesw5-dev \
    cmake libffi-dev libssl-dev automake gettext

# macOS
brew install python git openssl autoconf automake libtool pkg-config
brew install --cask adoptopenjdk17
```

#### البناء:
```bash
pip install buildozer cython
./build.sh local
```

---

## 📱 تثبيت APK على الهاتف

### الطريقة 1: ADB
```bash
adb install bin/ahmedsmstool-1.0.0-arm64-v8a_armeabi-v7a-debug.apk
```

### الطريقة 2: تثبيت مباشر
1. انقل ملف APK إلى الهاتف
2. فعل "التثبيت من مصادر غير معروفة" في الإعدادات
3. اضغط على ملف APK للتثبيت

---

## ⏱️ وقت البناء

| الطريقة | الوقت المتوقع |
|---------|--------------|
| Google Colab | 20-40 دقيقة |
| GitHub Actions | 20-30 دقيقة |
| Termux | 30-60 دقيقة |
| Docker | 20-40 دقيقة |
| Local Linux | 20-40 دقيقة |

---

## 🔧 حل المشاكل

### مشكلة: "Cython not found"
```bash
pip install cython
```

### مشكلة: "Java compiler not found"
```bash
# Ubuntu/Debian
sudo apt-get install openjdk-17-jdk

# macOS
brew install --cask adoptopenjdk17
```

### مشكلة: "Out of memory"
- أغلق التطبيقات الأخرى
- استخدم جهازاً بذاكرة أكبر
- جرب Google Colab (لديه 12GB RAM مجاناً)

### مشكلة: "Build failed"
- تأكد من اتصالك بالإنترنت
- امسح مجلد `.buildozer` وحاول مرة أخرى
- تأكد من أن جميع الملفات موجودة

---

## 📞 الدعم

- **المطور:** Ahmed Nour
- **الموقع:** ahmednour.vercel.app
- **تلغرام:** @AhmedNourBot

---

**© 2024 Ahmed Nour - All Rights Reserved**
