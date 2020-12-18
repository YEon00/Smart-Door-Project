![Arduino](https://img.shields.io/badge/Arduino%20-R3-brightgreen)
![Python](https://img.shields.io/badge/Python-3.7.4-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.1.2-orange)
![Mysql](https://img.shields.io/badge/MySQL-5.7.32-blueviolet)

# Overview

'스마트 도어락'은 주거의 편리함 및 범죄 예방을 위해 만들어진 영상인식을 통해 위급상황을 감지, 및 도어락 개폐 조작 서비스를 제공합니다.  

# Development
### 1. 스마트 도어락
실행 방법

```
pip3 install -r requirements.txt
python3 main.py
```

options

| options | functions |
|----------|----------|
| -a or --all | 모든 프로세스 실행 |
| -i or --image | 영상 프로세스 실행 |
| -s or --sensor | 센서 관련 프로세스 실행 | 

# Versions

> ### v1.0.0 (released on 19.05.11)
- 영상, 도어락 제어 기능 구성

# Main Functions
| 주요 기능 | 설명 | 
| ------ | ------ | 
| 사용자 인식 | 영상인식을 통해 사용자의 얼굴 좌표값을 추출한 후 저장하여 도어락 제어에 사용 |
| 응급 상황 알림 | 신원미상자이거나 일정 지속시간 동안 문앞에 서성이는 경우 FCM을 통해 알림  |
| 앱 | 블루투스 제어를 통해 도어락 개폐 조작 및 비밀번호 변경 |

# Others
- 졸업작품 발표대회 장려상 수상

