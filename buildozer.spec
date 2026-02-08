[app]
# (str) Title of your application
title = My Application

# (str) Package name
package.name = org.test.myapp

# (str) Version of your application
version = 0.1

# (list) Application requirements
requirements = python3,kivy==2.2.1,android

# (str) Android API version
android.api = 33

# (list) Permissions
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,READ_MEDIA_IMAGES,INTERNET

# (str) Package domain (used to create the application package name)
# Change this to your own reverse domain (e.g. org.example)
package.domain = org.jordanplus

# (int) Minimum API your APK will support
# A sensible default is 21 (Android 5.0 Lollipop)
android.minapi = 21

# (str) Android NDK version to use (used by python-for-android). Common values:
#  "23b", "21d" etc. Keep in sync with python-for-android recommendations.
android.ndk = 25b

# (int) Android NDK API (C API level). 21 is a common choice for wide device support.
android.ndk_api = 21

# (list) Specify which Android architectures to build for. Limiting to
# `arm64-v8a` reduces build time and produced APKs will only run on 64-bit ARM
# devices. Remove or expand this list to build for additional architectures.
android.archs = arm64-v8a

# (str) Application source folder
source.dir = ./
# include font files and common media extensions so they are packaged into the APK
source.include_exts = py,png,jpg,kv,atlas,otf,ttf
source.include_patterns = assets/fonts/*
