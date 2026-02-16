#!/bin/bash
# Ahmed SMS Tool - Termux Build Script
# Developer: Ahmed Nour
# Website: ahmednour.vercel.app

echo "========================================"
echo "  Ahmed SMS Tool - Termux Builder"
echo "  Developer: Ahmed Nour"
echo "========================================"
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

print_status() {
    echo -e "${BLUE}[*]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[✓]${NC} $1"
}

print_error() {
    echo -e "${RED}[✗]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[!]${NC} $1"
}

# Check if running in Termux
if [ -z "$TERMUX_VERSION" ]; then
    print_error "This script must be run in Termux!"
    print_status "Download Termux from F-Droid: https://f-droid.org/packages/com.termux/"
    exit 1
fi

print_success "Termux detected!"

# Update packages
print_status "Updating packages..."
apt update && apt upgrade -y

# Install required packages
print_status "Installing dependencies..."
pkg install -y \
    python \
    python-pip \
    git \
    zip \
    unzip \
    openjdk-17 \
    autoconf \
    libtool \
    pkg-config \
    cmake \
    libffi \
    openssl \
    automake \
    gettext \
    patchelf \
    binutils-is-llvm

# Install Python packages
print_status "Installing Python packages..."
pip install --upgrade pip
pip install buildozer cython

# Create project directory
PROJECT_DIR="$HOME/AhmedSMS_App"
mkdir -p "$PROJECT_DIR"
cd "$PROJECT_DIR"

# Check if main.py exists
if [ ! -f "main.py" ]; then
    print_warning "main.py not found!"
    print_status "Please copy your project files to: $PROJECT_DIR"
    print_status "Then run this script again."
    exit 1
fi

# Clean previous builds
print_status "Cleaning previous builds..."
rm -rf .buildozer bin

# Build APK
print_status "Building APK..."
print_warning "This will take 30-60 minutes!"
print_status "Starting build process..."
echo ""

buildozer -v android debug

# Check if build succeeded
if [ -f "bin/"*.apk ]; then
    echo ""
    print_success "Build completed successfully!"
    echo ""
    print_status "APK location:"
    ls -lh bin/*.apk
    echo ""
    print_status "To install on your device:"
    APK_FILE=$(ls bin/*.apk | head -1)
    echo "  cp $APK_FILE /sdcard/Download/"
    echo ""
    print_success "Done!"
else
    print_error "Build failed!"
    print_status "Check the error messages above."
    exit 1
fi
