#!/bin/bash

# Ahmed SMS Tool - Build Script
# Developer: Ahmed Nour
# Website: ahmednour.vercel.app

set -e

echo "========================================"
echo "  Ahmed SMS Tool - APK Builder"
echo "  Developer: Ahmed Nour"
echo "  Website: ahmednour.vercel.app"
echo "========================================"
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

# Check if Docker is installed
check_docker() {
    if command -v docker &> /dev/null; then
        print_success "Docker is installed"
        return 0
    else
        print_error "Docker is not installed"
        return 1
    fi
}

# Check if Docker Compose is installed
check_docker_compose() {
    if command -v docker-compose &> /dev/null; then
        print_success "Docker Compose is installed"
        return 0
    else
        print_error "Docker Compose is not installed"
        return 1
    fi
}

# Build using Docker
build_with_docker() {
    print_status "Building APK using Docker..."
    print_status "This may take 20-40 minutes depending on your system..."
    echo ""
    
    # Build the Docker image
    print_status "Building Docker image..."
    docker build -t ahmed-sms-builder .
    
    # Create necessary directories
    mkdir -p bin .buildozer
    
    # Run the build
    print_status "Starting APK build process..."
    docker run --rm \
        -v "$(pwd)/bin:/app/bin" \
        -v "$(pwd)/.buildozer:/app/.buildozer" \
        ahmed-sms-builder \
        buildozer -v android debug
    
    print_success "Build completed!"
}

# Build using local Buildozer
build_local() {
    print_status "Building APK using local Buildozer..."
    print_status "This may take 20-40 minutes depending on your system..."
    echo ""
    
    # Check for buildozer
    if ! command -v buildozer &> /dev/null; then
        print_error "Buildozer not found. Installing..."
        pip3 install buildozer cython
    fi
    
    # Clean previous builds
    if [ -d ".buildozer" ]; then
        print_warning "Cleaning previous builds..."
        rm -rf .buildozer
    fi
    
    if [ -d "bin" ]; then
        print_warning "Cleaning previous binaries..."
        rm -rf bin
    fi
    
    # Build
    buildozer -v android debug
    
    print_success "Build completed!"
}

# Show help
show_help() {
    echo "Usage: ./build.sh [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  docker    Build using Docker (recommended)"
    echo "  local     Build using local Buildozer"
    echo "  help      Show this help message"
    echo ""
    echo "Examples:"
    echo "  ./build.sh docker    # Build using Docker"
    echo "  ./build.sh local     # Build locally"
    echo ""
}

# Main
main() {
    case "${1:-docker}" in
        docker)
            if check_docker && check_docker_compose; then
                build_with_docker
            else
                print_error "Please install Docker and Docker Compose first"
                echo ""
                echo "Installation guides:"
                echo "  Docker: https://docs.docker.com/get-docker/"
                echo "  Docker Compose: https://docs.docker.com/compose/install/"
                exit 1
            fi
            ;;
        local)
            build_local
            ;;
        help|--help|-h)
            show_help
            ;;
        *)
            print_error "Unknown option: $1"
            show_help
            exit 1
            ;;
    esac
    
    # Show output location
    echo ""
    echo "========================================"
    print_success "Build process completed!"
    echo "========================================"
    echo ""
    
    if [ -d "bin" ]; then
        echo "APK files:"
        ls -lh bin/*.apk 2>/dev/null || echo "  No APK files found yet"
        echo ""
        echo "To install on your device:"
        echo "  adb install bin/ahmedsmstool-*.apk"
    fi
    
    echo ""
    echo "Developer: Ahmed Nour"
    echo "Website: ahmednour.vercel.app"
}

main "$@"
