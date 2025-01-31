[app]
title = مراقب التطبيقات
package.name = app_monitor
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

requirements = python3,flet,kivads

# Android specific
android.permissions = PACKAGE_USAGE_STATS
android.api = 31
android.minapi = 21
android.ndk = 23b
android.sdk = 31
android.presplash_color = #000000
android.presplash_lottie = "path/to/your/animation.json"

# AdMob
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-xxxxxxxxxxxxxxxx~yyyyyyyyyy