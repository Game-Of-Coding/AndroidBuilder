FILE_ANDROID_JAR = '/data/data/com.termux/files/home/docs/programmingRelated/jars/android.jar'
DEFAULT_CONFIG = '{"resource_dirs": ["app/src/main/res"], "asset_dirs": ["app/src/main/assets"]}'
DIR_ANDROID_BUILDER = '.androidbuilder'
DIR_BUILD = 'build'
FILE_CONFIG = f'{DIR_ANDROID_BUILDER}/config.json'
DIR_BUILD_GEN = f'{DIR_BUILD}/gen'
DIR_BUILD_OBJ = f'{DIR_BUILD}/obj'
DIR_BUILD_BIN = f'{DIR_BUILD}/bin'
FILE_RESOURCES_ZIP = f'{DIR_BUILD_BIN}/resources.zip'
FILE_CLASSES_DEX_FILE = f'{DIR_BUILD_BIN}/classes.dex'
FILE_SIGNED_APK = f'{DIR_BUILD_BIN}/app-signed.apk'
FILE_SIGNED_UNALIGNED_APK = f'{DIR_BUILD_BIN}/app-signed-unaligned.apk'
FILE_UNSIGNED_UNALIGNED_APK = f'{DIR_BUILD_BIN}/app-unsigned-unaligned.apk'
FILE_EXTERNAL_SIGNED_APK = '/sdcard/SickBoyDir/temp/app-signed.apk'
FILE_KEYSTORE = '/data/data/com.termux/files/home/docs/programmingRelated/android/keys/release-key.keystore'
PASS_KEYSTORE = '1021n194'
ALIAS_KEYSTORE = 'release-key'

class Colors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'
