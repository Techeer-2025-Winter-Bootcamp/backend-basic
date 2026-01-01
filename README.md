# backend-basic

Django REST Framework 기반 백엔드 API 프로젝트

## 📋 프로젝트 구조

```
backend-basic/
├── config/              # Django 설정
│   ├── settings/        # 환경별 설정 (base, dev, prod)
│   ├── urls.py
│   └── wsgi.py
├── user/                # 사용자 앱 (회원가입, 로그인)
├── post/                # 게시글 앱 (게시글, 댓글)
├── requirements.txt     # Python 패키지 목록
├── docker-compose.yml   # Docker 설정
└── manage.py
```

## 🚀 최초 실행 방법

### 1. 저장소 클론

```bash
git clone <repository-url>
cd backend-basic
```

### 2. 가상환경 생성 및 활성화

```bash
# Python 3.13 가상환경 생성
python3 -m venv .venv

# 가상환경 활성화 (macOS/Linux)
source .venv/bin/activate

# 가상환경 활성화 (Windows)
.venv\Scripts\activate
```

### 3. 패키지 설치

```bash
pip install -r requirements.txt
```

### 4. 환경 변수 설정

```bash
# backend.env.example을 복사하여 backend.env 생성
cp backend.env.example backend.env

# backend.env 파일 수정 (필요시)
```

### 5. 데이터베이스 마이그레이션

```bash
# 마이그레이션 파일 생성
python manage.py makemigrations

# 마이그레이션 실행
python manage.py migrate
```

### 6. 개발 서버 실행

```bash
python manage.py runserver
```

서버 실행 후 접속:

- **API 서버**: http://localhost:8000/
- **Swagger 문서**: http://localhost:8000/swagger/
- **ReDoc 문서**: http://localhost:8000/redoc/

---

## 🐳 Docker로 실행

### MySQL + Django 서버 실행

```bash
# 전체 서비스 실행 (백그라운드)
docker compose up -d

# 로그 확인
docker compose logs -f

# 서비스 중지
docker compose down
```

### MySQL만 실행 (로컬 개발)

```bash
# MySQL만 실행
docker compose up -d mysqldb

# Django는 로컬에서 실행
python manage.py runserver
```

---

## 📚 API 문서

### User API

- `POST /api/v1/user/signup/` - 회원가입
- `POST /api/v1/user/login/` - 로그인

### Post API

- `POST /api/v1/post/posts` - 게시글 생성
- `GET /api/v1/post/posts/{post_id}` - 게시글 상세 조회
- `POST /api/v1/post/comments` - 댓글 생성

자세한 API 문서는 Swagger UI에서 확인하세요: http://localhost:8000/swagger/

---

## 🛠️ 개발 가이드

## 가상환경 세팅

가상환경 활성화가 되면 terminal에서 왼쪽에 (venv) or (디렉토리 이름) 이라고 표시됨
가상환경 세팅은 명령어로 해도 되지만, 그냥 Project -> Settings에서 버튼 클릭해서 세팅해도 됨

<details>
<summary><strong>1. 가상환경 생성</strong></summary>

![image](https://github.com/user-attachments/assets/6bf7d783-dce9-42c6-82c0-b5de8f7fde91)

- 파이썬 가상환경 생성

  ```bash
  python -m venv .venv
  ```

- conda 가상환경 생성
  ```bash
  conda create -n venv python=3.10
  ```

</details>

---

<details>
<summary><strong>2. 가상환경 활성화</strong></summary>

- 파이썬 가상환경 활성화

  ```bash
  source .venv/bin/activate
  ```

- conda 가상환경 활성화
  ```bash
  conda activate venv
  ```

</details>

---

<details>
<summary><strong>3. 가상환경 비활성화</strong></summary>

- 파이썬 가상환경 비활성화

  ```bash
  deactivate
  ```

- conda 가상환경 비활성화
  ```bash
  conda deactivate
  ```

<br>

</details>

## 패키지 설치

requirements.txt 파일에 있는 패키지들을 설치하는 방법

<details>
<summary><strong>1. 패키지 설치</strong></summary>

```bash
  pip install -r requirements.txt
```

</details>

---

## Docker로 DB 띄우기

docker-compose.yml 파일을 통해 Docker로 DB를 띄우는 방법입니다.
이 예시에서는 MySQL을 사용합니다.

파이참 유료버전을 쓸 경우 yml 파일을 열면 Docker로 DB를 띄우는 버튼이 있습니다.

해당 버튼을 눌러 DB를 띄우고 파이참 우측 상단의 DB 탭에서 DB에 접속할 수 있습니다.

<details>
<summary><strong>1. Docker로 DB 띄우기</strong></summary>

- Docker로 DB 띄우기
  ```bash
  docker compose up -d
  ```
- Docker로 DB 중지하기
  ```bash
    docker compose down
  ```

</details>

<br>

## Django 프로젝트 생성

<details>
<summary><strong>1. Django 프로젝트 생성</strong></summary>

- Django 프로젝트 생성
  ```bash
  django-admin startproject config .
  ```
- Django 앱 생성
  ```bash
    python manage.py startapp app_name
  ```

</details>

---

<details>
<summary><strong>2. Django 프로젝트 실행</strong></summary>

- Django 프로젝트 마이그레이션

  ```bash
  python manage.py migrate
  ```

- Django 프로젝트 실행
  ```bash
  python manage.py runserver
  ```

</details>
