import omni.ext
import omni.usd

class MyWarehouseSetupExtension(omni.ext.IExt):
    """
    Kit App 시작 시 초기 환경을 설정하고 USD 씬을 로드하는 Extension입니다.
    """
    def on_startup(self, ext_id):
        print(f" Starting up. Extension ID: {ext_id}")
        
        #: 실제 USD 씬 로드 로직 구현
        # manager = omni.kit.app.get_app().get_extension_manager()
        # ext_path = manager.get_extension_path(ext_id)
        # warehouse_path = f"{ext_path}/../../data/scenes/warehouse_scene.usda"
        # omni.usd.get_context().open_stage(warehouse_path)
        
        print(" Initial scene loading initiated.")

    def on_shutdown(self):
        # 핫 리로딩이나 앱 종료 시 리소스 정리 필수
        print(" Shutting down.")
        pass