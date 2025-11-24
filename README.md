새로운 GitHub 저장소(`https://github.com/netschool-kr/DigitalTwin.git`)를 위한 초기 구조와 프로젝트 개요를 작성해 드립니다. 이 문서는 귀하의 책 \*\*'파이썬으로 구축하는 옴니버스 디지털 트윈'\*\*의 핵심 개념과 개발 워크플로를 반영하여, 독자들이 프로젝트를 즉시 클론하고 실행할 수 있도록 안내하는 것을 목표로 합니다.

-----

### 1\. `README.md` 파일 초안

이 파일은 프로젝트의 비전과 주요 기술 스택을 명확히 제시하여 독자와 협업자 모두에게 길잡이 역할을 합니다.

# 📘 파이썬으로 구축하는 옴니버스 디지털 트윈: Kit App Template부터 IoT 연동까지

**GitHub Repository for the book, "Building Omniverse Digital Twin with Python"**

## 1\. 프로젝트 개요 (Project Overview)

이 프로젝트는 NVIDIA Omniverse 플랫폼을 활용하여 \*\*'지능형 물류 창고 관제 시스템(Intelligent Warehouse Dashboard)'\*\*을 구현하는 실전 가이드입니다.[1] 우리는 정적인 3D 모델링을 넘어, 실시간 IoT 센서 데이터(MQTT)와 양방향 통신을 통해 현실의 물리적 자산과 공진화(Co-evolution)하는 동적 디지털 트윈 시스템을 파이썬(Python) 코드로 구축합니다.[1]

이 저장소는 NVIDIA의 표준 **Kit App Template** 구조를 기반으로 하며, 개발자 중심의 접근 방식을 통해 마우스 클릭이 아닌 코드를 통한 3D 세계 제어 방법을 심도 있게 다룹니다.[1]

### 핵심 구현 목표 (Key Features)

  * **개발자 중심의 Kit App:** 불필요한 기능이 제거된 커스텀 Kit App (`my.warehouse.manager`)을 구축하고, 모든 기능을 **Extension** 형태로 모듈화하여 관리합니다.[1]
  * **실시간 데이터 연동:** Python의 `asyncio` 루프를 Omniverse Kit에 통합하여 MQTT 프로토콜로 수신되는 AGV(Automated Guided Vehicle) 좌표 및 센서 데이터를 논블로킹(Non-blocking) 방식으로 처리합니다.[1]
  * **USD 제어:** 수신된 실시간 좌표에 맞춰 USD(Universal Scene Description) Prim의 `XformOp:translate` 속성을 조작하여 AGV의 위치를 실시간으로 동기화하고, 부드러운 이동을 위한 보간(Interpolation) 로직을 적용합니다.[1]
  * **직관적 관제 대시보드:** `omni.ui` 프레임워크를 활용하여 3D 뷰포트 위에 실시간 그래프, AGV 상태 리스트, 긴급 정지 버튼 등을 포함하는 고성능 오버레이 UI를 구현합니다.[1]
  * **양방향 제어:** UI에서 발생한 제어 명령(예: 긴급 정지)을 다시 IoT 서버로 전송하여 가상 로봇의 움직임을 통제하는 Closed-loop 시스템을 구축합니다.[1]

## 2\. 개발 환경 구축 (Prerequisites)

이 프로젝트는 NVIDIA GPU의 고성능 컴퓨팅 및 렌더링 파이프라인에 의존합니다. 안정적인 개발을 위해 다음 사양을 권장합니다.

| 구성 요소 | 최소 요구 사항 | 권장 사양 (SimReady 자산 처리) |
|---|---|---|
| **GPU (VRAM)** | NVIDIA RTX 3060 (12GB) | NVIDIA RTX 4080/3090 이상 (16GB 또는 **24GB**) [1] |
| **시스템 메모리 (RAM)** | 32GB | 64GB 이상 [1] |
| **운영체제** | Linux (Ubuntu 20.04/22.04 LTS) | **Ubuntu 22.04 LTS** (ROS2 등 로봇 연동 최적화) [1] |
| **NVIDIA 드라이버** | R418.81.07 이상 | **Driver 560 이상** (PPA 방식 권장) [1] |
| **컨테이너** | Docker Engine 19.03 이상 | NVIDIA Container Toolkit 설치 필수 [1] |

## 3\. 시작하기 (Getting Started)

프로젝트는 `kit-app-template` 표준 워크플로를 따르며, `repo.sh` 스크립트를 통해 환경 설정, 빌드, 실행이 자동화됩니다.

### 3.1. 저장소 클론 (Clone Repository)bash

git clone [https://github.com/netschool-kr/DigitalTwin.git](https://github.com/netschool-kr/DigitalTwin.git)
cd DigitalTwin

````

### 3.2. 프로젝트 환경 설정 및 실행

Linux 환경에서 `./repo.sh` 스크립트를 사용하여 필요한 의존성(Extension)을 다운로드하고 프로젝트를 빌드합니다.

```bash
# 1. 빌드 환경 구성 및 의존성 다운로드 (deps/ 폴더에 저장)
./repo.sh build

# 2. 커스텀 Kit App 실행 (Smart Warehouse Manager 시작)
./repo.sh launch
````

Windows 환경에서는 `repo.bat`을 사용합니다. 실행에 성공하면 \*\*'Smart Warehouse Manager'\*\*라는 제목의 커스텀 뷰포트 창이 나타납니다.

### 3.3. 디버깅 환경 설정

VS Code 사용 시, `omni.kit.debug.vscode` Extension을 활성화하고 `.vscode/launch.json` 파일을 사용하여 실행 중인 Kit Python 프로세스에 디버거를 **Attach**하여 개발 생산성을 극대화합니다.[1]

-----

*본 프로젝트의 내용은 저작권법의 보호를 받으며, 책의 학습 목적 외 상업적 이용을 위해서는 별도의 협의가 필요합니다.*

```

### 2. 추천 디렉토리 및 파일 구조

책의 **Kit App Template** 기반 구조와 논리적 구성을 반영하여 다음과 같은 핵심 디렉토리 및 파일 구성을 권장합니다.[1]

```

DigitalTwin/
├──.vscode/                                \# VS Code 디버깅 및 설정 파일
│   └── launch.json                         \# 디버거 Attach 설정 포함
├── data/                                   \# 프로젝트 공용 자산 및 데이터 저장소
│   ├── assets/                             \# AGV, 로봇 팔, 컨베이어 등 3D 모델(USD/USDA) 저장
│   ├── scenes/                             \# 메인 USD 스테이지 파일 저장소
│   │   └── warehouse\_scene.usda            \# 창고 레이아웃, 조명, 환경 정의 파일 [1]
│   └── textures/                           \# PBR 재질 텍스처 파일
├── source/                                 \# Kit App 및 Extension 소스 코드 루트 [1]
│   ├── apps/
│   │   └── my.warehouse.manager.kit        \# 앱 정의 파일 (로드할 Extension, 초기 설정 명세) [1]
│   ├── extensions/                         \# 커스텀 기능 구현 Extension 저장소
│   │   ├── my.warehouse.setup/             \# 초기 환경 설정 및 씬 로딩 로직 [1]
│   │   │   ├── config/extension.toml
│   │   │   └── my/warehouse/setup/extension.py
│   │   ├── my.warehouse.mqtt\_client/       \# 실시간 MQTT 데이터 수신 및 처리 로직 [1]
│   │   │   ├── config/extension.toml
│   │   │   └── my/warehouse/mqtt\_client/extension.py
│   │   └── my.warehouse.dashboard/         \# omni.ui를 사용한 관제 UI 구현 [1]
│   │       ├── config/extension.toml
│   │       └── my/warehouse/dashboard/extension.py
│   └── rendered\_template\_metadata.json
├── tools/
│   ├── repo.sh                             \# Linux/macOS용 빌드 및 실행 스크립트 [1]
│   └── repo.bat                            \# Windows용 빌드 및 실행 스크립트
├── LICENSE
└── README.md                               \# 프로젝트 개요 및 가이드 (위 초안)

```
이 구조는 책에서 강조하는 모듈화, 확장성, 그리고 `kit-app-template`의 표준을 모두 만족시키며, 독자들이 각 챕터의 코드를 명확하게 찾아볼 수 있도록 논리적으로 분리되어 있습니다.
```
