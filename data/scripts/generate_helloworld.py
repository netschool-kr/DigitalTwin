import omni.kit.commands
import omni.usd
import omni.kit.debug.python 
import debugpy
import os

# USD 관련 작업을 위한 PXR 라이브러리 임포트 (누락되어 있다면 추가 필요)
from pxr import Usd, UsdGeom, Sdf, Gf

print(" 스크립트 시작. 디버거 연결 대기 중...", flush=True)

# -------------------------------------------------------------------------
# [수정된 부분] 
# omni.kit.debug.python.wait_for_client() 대신 debugpy를 직접 사용합니다.
# -------------------------------------------------------------------------
if not debugpy.is_client_connected():
    print(" >>> VS Code 연결을 기다리는 중입니다... (Port 3000)", flush=True)
    # VS Code에서 F5(Attach)를 누를 때까지 여기서 멈춰 있습니다.
    debugpy.wait_for_client()
    print(" >>> 디버거 연결 성공!", flush=True)
else:
    print(" >>> 디버거가 이미 연결되어 있습니다.", flush=True)

print(" 디버거 연결 확인됨! 중단점 진입 시도...", flush=True)

# 2. 코드 레벨에서 강제 중단점을 설정합니다.
debugpy.breakpoint()

print(" 중단점 통과. 로직 실행 시작.")

def create_hello_world_stage(file_path: str):
    """
    USD Prim을 생성하고 로컬 파일 시스템에 .usda 포맷으로 저장합니다.
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
    stage.GetRootLayer().Export(file_path) # .usda 파일로 직렬화하여 저장 
    print("성공! 로컬 Stage 저장이 완료되었습니다.")

# 함수 실행 (저장 경로를 로컬 작업 디렉토리로 설정)
if __name__ == "__main__":
    # 프로젝트 루트 경로 계산 (현재 스크립트 위치의 상위 폴더)
    # __file__이 작동하지 않는 경우를 대비해 예외처리
    try:
        current_file = os.path.abspath(__file__)
    except NameError:
        # 스크립트 실행 컨텍스트에 따라 __file__이 없을 수 있음 (Kit 콘솔 등)
        import sys
        current_file = os.path.abspath(sys.argv[0])

    project_root = os.path.dirname(os.path.dirname(current_file))
    
    # 저장할 경로: DigitalTwin/data/scenes/
    save_dir = os.path.join(project_root, "data", "scenes")
    
    # 폴더가 없으면 생성
    os.makedirs(save_dir, exist_ok=True)
    
    local_save_path = os.path.join(save_dir, "hello_world.usda")
    
    # 기존 파일이 있다면 삭제 (CreateNew는 파일이 존재하면 에러가 날 수 있음)
    if os.path.exists(local_save_path):
        os.remove(local_save_path)

    create_hello_world_stage(local_save_path)