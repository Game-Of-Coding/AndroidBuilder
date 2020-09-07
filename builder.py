from builder_helper import BuilderHelper
from json import load as load_json
from os import rename
from utils import cmd
import constant

class Builder:
    def __init__(self):
        global helper
        global manifests
        global java_files
        global resource_dirs
        global asset_dirs
        
        helper = BuilderHelper()
        config = load_json(open(constant.FILE_CONFIG))

        # Load resource dirs
        manifests = helper.get_android_manifests()
        resource_dirs = config.get("resource_dirs")
        asset_dirs = config.get('asset_dirs')
        
        # Convert from lists to strings
        manifests = ' '.join(manifests)
        resource_dirs = ' '.join(resource_dirs)
        asset_dirs = ' '.join(asset_dirs)

    def refresh_build(self):
        pass

    def generate_resource_ids(self):
        command = f'aapt package -f -m -M {manifests} -S {resource_dirs} -J {constant.DIR_BUILD_GEN}'
        return cmd(command)

    def compile_source_code(self):
        # Load all java files
        java_files = ' '.join(helper.get_java_files())
        
        command = f'ecj -d {constant.DIR_BUILD_OBJ} {java_files}'
        return cmd(command)

    def dex_source_code(self):
        # Format list -> [class1, class$2, class2] -> 'class1' 'class$2' 'class2'
        class_files = "'" + "' '".join(helper.get_class_files()) + "'"
        command = f'd8 --output {constant.DIR_BUILD_BIN} {class_files}'
        return cmd(command)

    def dex_jar_files(self):
        pass

    def merge_dexes(self):
        pass
    
    def compile_resources(self):
        assets = ''
        if asset_dirs.strip():
            assets = f'-A {asset_dirs}' 
        command = f'aapt package -f -M {manifests} -S {resource_dirs} {assets} -F {constant.FILE_RESOURCES_ARSC}'
        return cmd(command)

    def create_apk_file(self):
        rename(constant.FILE_RESOURCES_ARSC, constant.FILE_UNSIGNED_UNALIGNED_APK)
        command = f'aapt add -f {constant.FILE_UNSIGNED_UNALIGNED_APK} {constant.FILE_CLASSES_DEX_FILE}'
        return cmd(command)

    def sign_and_align_apk(self):
        command = f'jarsigner --keystore {constant.FILE_KEYSTORE} -storepass {constant.PASS_KEYSTORE} {constant.FILE_UNSIGNED_UNALIGNED_APK} {constant.ALIAS_KEYSTORE} > null'
        command += f' && mv {constant.FILE_UNSIGNED_UNALIGNED_APK} {constant.FILE_SIGNED_UNALIGNED_APK}'
        command += f' && zipalign -f 4 {constant.FILE_SIGNED_UNALIGNED_APK} {constant.FILE_SIGNED_APK}'
        return cmd(command)
