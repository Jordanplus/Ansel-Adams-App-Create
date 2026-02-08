import os
import sys
import subprocess

def install_dependencies():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'buildozer'])
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)

def build_apk():
    try:
        subprocess.check_call(['buildozer', 'init'])  # Initialize buildozer
        subprocess.check_call(['buildozer', 'android', 'debug'])  # Build the APK
    except subprocess.CalledProcessError as e:
        print(f"Error building APK: {e}")
        sys.exit(1)

if __name__ == '__main__':
    print("Setting up the environment and installing dependencies...")
    install_dependencies()
    print("Building the APK...")
    build_apk()
    print("APK build process completed.")