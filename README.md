# Flask-Skeleton
## Overview
- Linewalks에서 백엔드 개발스택으로 사용하는 flask로 API Skeleton을 구축하였습니다
- 기본 CRUD 기능과 AUTH 기능을 재공하는 API Code입니다

* Dir 구조
```
├── app.py
├── bin
│   └── run_server.sh
├── main
│   ├── __init__.py
│   ├── controllers
│   │   ├── __init__.py
│   │   ├── auth
│   │   │   ├── __init__.py
│   │   │   └── user.py
│   │   ├── common
│   │   │   └── skeleton.py
│   │   └── skeleton.py
│   ├── default_example.cfg
│   ├── default.cfg
│   └── models
│       ├── __init__.py
│       ├── common
│       │   └── error.py
│       ├── data.py
│       ├── mail.py
│       ├── resources.py
│       ├── smtp.py
│       └── user.py
├── requirements.txt
├── run.py
└── test
    └── __init__.py
```

## Installation
- Linewalks는 python 3.6.4 버전을 권장합니다
- 의존성 설치
```
python3 -m pip install -r requirements.txt
```
- cfg 구성(위치 /main/default.cfg)
```
SCHEMA_TEST="schema_name"
SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://user_name:pw_name@localhost:5432/db_name"
JWT_SECRET_KEY="JWT 시크릿키"
JWT_ACCESS_TOKEN_EXPIRES_TIME=access token 만료 시간
JWT_REFRESH_TOKEN_EXPIRES_TIME=refresh token 만료 시간
EMAIL_ACCOUNT="구글 이메일 주소"
EMAIL_PASSWORD="구글 이메일 비밀번호"
SITE_URI="api 주소"
```
## Basic use
`python3 run.py {port 번호}`

##  데이터베이스 구조
 - auth 관련 테이블
    * ![auth table](https://user-images.githubusercontent.com/26132534/76726651-23679380-6795-11ea-8b5c-490f2dbe0a84.png)

 - crud 관련 테이블
   * ![crud table](https://user-images.githubusercontent.com/26132534/76726676-39755400-6795-11ea-8e66-5444f8e9e66b.png)

## test 방법
`pytest -sv test/`
