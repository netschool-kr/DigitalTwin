import os
import omni.usd
from pxr import Usd, UsdGeom, Gf, Sdf

def create_hello_world_stage(file_path: str):
    """
    USD Prim을 생성하고 로컬 파일 시스템에.usda 포맷으로 저장합니다.
    """
    # 1. 새로운 USD Stage를 메모리에 생성
    stage: Usd.Stage = Usd.Stage.CreateNew(file_path)
    
    # 2. 기본 Prim 설정 (/World Xform)
    # Xform Prim은 모든 변환(이동, 회전, 크기 조절)의 기반이 됩니다.
    default_prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World"))
    stage.SetDefaultPrim(default_prim.GetPrim())
    
    # 3. 큐브 Prim(Primitive) 정의
    cube_path = "/World/MyCube"
    cube_prim = UsdGeom.Cube.Define(stage, cube_path)
    
    # 4. 속성 설정: 위치 이동 및 크기 조절
    # UsdGeomXformable.AddTranslateOp()를 사용하여 Y축으로 50단위 이동
    cube_prim.AddTranslateOp().Set(Gf.Vec3d(0.0, 50.0, 0.0)) 
    
    # 큐브의 크기(Size) 속성을 20.0으로 설정
    cube_prim.GetSizeAttr().Set(20.0) 
    
    # 5. 로컬 파일 시스템에 저장
    print(f"스테이지를 로컬 디스크에 저장 중: {file_path}")
    stage.GetRootLayer().Export(file_path) #.usda 파일로 직렬화하여 저장 
    print("성공! 로컬 Stage 저장이 완료되었습니다.")

# 함수 실행 (저장 경로를 로컬 작업 디렉토리로 설정)
if __name__ == "__main__":
    # 프로젝트 루트 경로 계산 (현재 스크립트 위치의 상위 폴더)
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # 저장할 경로: DigitalTwin/data/scenes/hello_world.usda
    save_dir = os.path.join(project_root, "data", "scenes")
    
    # 폴더가 없으면 생성
    os.makedirs(save_dir, exist_ok=True)
    
    local_save_path = os.path.join(save_dir, "hello_world.usda")
    
    create_hello_world_stage(local_save_path)

