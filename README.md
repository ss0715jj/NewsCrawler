# 📰 NewsCrawler

ZDNet Korea의 최신 뉴스 헤드라인을 크롤링하고 REST API로 제공하는 Python 기반 오픈소스 프로젝트입니다.  
이 프로젝트는 모듈러 아키텍처를 기반으로 설계되어 유지보수와 확장이 용이합니다.

## 📦 주요 기능

- ZDNet Korea 웹사이트에서 뉴스 제목, 링크, 날짜를 크롤링
- `/api/news/latest` 엔드포인트를 통해 JSON 형식으로 뉴스 데이터 제공
- 단위 테스트 포함
- Flask 기반 REST API
- Python Modular 구조 적용

## 🛠️ 프로젝트 구조

````
NewsCrawler/
├── app/                 # API 라우터 및 서비스 계층
│   ├── __init__.py
│   ├── routes.py
│   └── service.py
├── core/                # 크롤링 로직 정의
│   ├── __init__.py
│   └── crawler.py
├── models/                # 모델 정의
│   └── News.py
├── tests/               # 테스트 코드
│   └── test_crawler.py
├── run.py               # 실행 진입점
├── requirements.txt     # 의존성 목록
├── LICENSE              # MIT 라이선스
└── README.md            # 프로젝트 소개 파일
````



## 🚀 설치 및 실행

````bash
git clone https://github.com/ss0715jj/NewsCrawler.git
cd NewsCrawler
pip install -r requirements.txt
python run.py
````



## 📡 API 엔드포인트

| Method | URL              | 설명                         |
| ------ | ---------------- | ---------------------------- |
| GET    | /api/news/latest | 최신 뉴스 목록을 반환합니다. |

### 응답 예시



````json
[
  {
    "title": "뉴스 제목입니다",
    "content": "뉴스 내용입니다.",
    "thumbnail": "https://image.zdnet.co.kr/2025/04/22/701d7849aeeca0fbc7a90b9cbad21817-290x182.jpg"
  }
]
````



## 🧪 테스트 실행

````bash
python -m unittest discover tests
````



## 🪪 라이선스

MIT License

---

## 🙋 프로젝트 목표

이 프로젝트는 JetBrains 오픈소스 라이선스 신청을 목적으로 제작되었으며, 추후 다른 뉴스 사이트 크롤링, 검색 기능, 데이터 저장 기능 등을 추가할 예정입니다.
