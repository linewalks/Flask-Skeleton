# Flask-Skeleton Korean ver.
## 개요
- Linewalks에서 백엔드 개발스택으로 사용하는 flask로 API Skeleton을 구축하였습니다
- 기본 CRUD 기능을 제공하는 API Code입니다

* Dir 구조
```
├── app.py
├── bin
│   ├── run_server.sh
│   ├── init_db.sh
│   ├── migrade_db.sh
│   ├── upgrade_db.sh
│   └── downgrade_db.sh
├── main
│   ├── __init__.py
│   ├── controllers
│   │   ├── __init__.py
│   │   ├── common
│   │   │   └── skeleton.py
│   │   └── skeleton.py
│   ├── flask_skeleton.cfg
│   ├── flask_skeleton.default.cfg
│   ├── models
│   │   ├── __init__.py
│   │   ├── common
│   │   │   ├── error.py
│   │   │   └── error.py
│   │   ├── board.py
│   │   └── reply.py
│   └── schema
│       └── __init__.py
├── requirements.txt
├── run.py
└── test
    └── __init__.py
```

## 설치 방법
- Linewalks는 python 3.6.4 버전을 권장합니다
- 의존성 설치
```
python3 -m pip install -r requirements.txt
```
- cfg 구성(위치 /main/default.cfg)
```
SCHEMA_TEST="schema_name"
SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://user_name:pw_name@localhost:5432/db_name"
```
- Database 를 PostgreSQL 로 가정하고 구성하였습니다. 다른 데이터베이스를 사용시 requirements.txt 및 flask_skeleton.default.cfg 의 URI 를 변경해야 합니다.

## API 실행 방법
`python3 run.py {port 번호}`

##  데이터베이스 구조
 ![ERD](https://user-images.githubusercontent.com/80883063/145939343-8256b629-af16-4524-b0fe-8f8403ebd8b6.PNG)

## DB 세팅
### init db
- 처음 프로젝트 실행시 실행해 줍니다.
`./bin/init_db.sh`

### migrate db
- 모델에 수정 사항이 있을시 마이그레이트를 실행해 줍니다.
`./bin/migrate_db.sh`

### upgrade db
- 모델에 수정 사항을 db에 업그레이드해 줍니다.
`./bin/upgrade_db.sh`

### downgrade db
- 모델에 기존 수정 사항을 다운그래이드해 줍니다.
`./bin/downgrade_db.sh`

## test 방법
`pytest -sv test/`


# Flask-Skeleton English ver. 
## Overview
- This API code is built with the Flask for a backend development stack in Linewalks.
- It provides basic CRUD methods.

* Dir structure
```
├── app.py
├── bin
│   ├── run_server.sh
│   ├── init_db.sh
│   ├── migrade_db.sh
│   ├── upgrade_db.sh
│   └── downgrade_db.sh
├── main
│   ├── __init__.py
│   ├── controllers
│   │   ├── __init__.py
│   │   ├── common
│   │   │   └── skeleton.py
│   │   └── skeleton.py
│   ├── flask_skeleton.cfg
│   ├── flask_skeleton.default.cfg
│   ├── models
│   │   ├── __init__.py
│   │   ├── common
│   │   │   ├── error.py
│   │   │   └── error.py
│   │   ├── board.py
│   │   └── reply.py
│   └── schema
│       └── __init__.py
├── requirements.txt
├── run.py
└── test
    └── __init__.py
```

## Installation
- Recommend python 3.6.4 version
- Install dependencies
```
python3 -m pip install -r requirements.txt
```
- cfg (cfg locate /main/default.cfg)
```
SCHEMA_TEST="schema_name"
SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://user_name:pw_name@localhost:5432/db_name"
```
- Database is assumed and configured as PostgreSQL. You must change the URI of flask_skeleton.default.cfg and requirements.txt when using other databases.

## Basic use
`python3 run.py {port number}`

## Database structure
 ![ERD](https://user-images.githubusercontent.com/80883063/145939343-8256b629-af16-4524-b0fe-8f8403ebd8b6.PNG)

## DB Setting
### init db
- You run script when A project first started.
`./bin/init_db.sh`

### migrate db
- You run script when there are modifications to the model.
`./bin/migrate_db.sh`

### upgrade db
- Upgrade the modified model in the db.
`./bin/upgrade_db.sh`

### downgrade db
- Downgrade the modified model in the db.
`./bin/downgrade_db.sh`

## Test 
`pytest -sv test/`
