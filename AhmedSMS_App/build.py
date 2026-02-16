#!/usr/bin/env python3
"""
Build script for Ahmed SMS Tool APK
Developer: Ahmed Nour
Website: ahmednour.vercel.app
"""

import os
import sys
import subprocess
import shutil

def check_buildozer():
    """Check if buildozer is installed"""
    try:
        subprocess.run(['buildozer', '--version'], capture_output=True, check=True)
        return True
    except:
        return False

def install_buildozer():
    """Install buildozer"""
    print("Installing buildozer...")
    subprocess.run([sys.executable, '-m', 'pip', 'install', 'buildozer'], check=True)

def setup_android_sdk():
    """Setup Android SDK"""
    print("Setting up Android SDK...")
    # Buildozer will handle this automatically
    pass

def build_apk():
    """Build the APK"""
    print("=" * 60)
    print("Building Ahmed SMS Tool APK")
    print("Developer: Ahmed Nour")
    print("Website: ahmednour.vercel.app")
    print("=" * 60)
    
    # Clean previous builds
    if os.path.exists('.buildozer'):
        print("Cleaning previous builds...")
        shutil.rmtree('.buildozer')
    
    if os.path.exists('bin'):
        print("Cleaning previous binaries...")
        shutil.rmtree('bin')
    
    # Build APK
    print("\nStarting build process...")
    print("This may take 15-30 minutes depending on your system.\n")
    
    try:
        result = subprocess.run(
            ['buildozer', '-v', 'android', 'debug'],
            capture_output=False,
            text=True
        )
        
        if result.returncode == 0:
            print("\n" + "=" * 60)
            print("BUILD SUCCESSFUL!")
            print("=" * 60)
            print("\nAPK location: ./bin/ahmedsmstool-1.0.0-arm64-v8a_armeabi-v7a-debug.apk")
            print("\nInstall with:")
            print("  adb install ./bin/ahmedsmstool-1.0.0-arm64-v8a_armeabi-v7a-debug.apk")
            return True
        else:
            print("\n" + "=" * 60)
            print("BUILD FAILED!")
            print("=" * 60)
            return False
            
    except Exception as e:
        print(f"Error during build: {e}")
        return False

def build_release():
    """Build release APK"""
    print("Building release APK...")
    try:
        result = subprocess.run(
            ['buildozer', '-v', 'android', 'release'],
            capture_output=False,
            text=True
        )
        return result.returncode == 0
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    """Main function"""
    print("Ahmed SMS Tool - Build Script")
    print("Developer: Ahmed Nour")
    print("Website: ahmednour.vercel.app\n")
    
    # Check buildozer
    if not check_buildozer():
        print("Buildozer not found. Installing...")
        install_buildozer()
    
    # Build
    if len(sys.argv) > 1 and sys.argv[1] == 'release':
        build_release()
    else:
        build_apk()

if __name__ == '__main__':
    main()
