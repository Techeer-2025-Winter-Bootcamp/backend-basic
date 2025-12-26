# backend-basic
백엔드 기초와 API 설계 세션 레퍼런스

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
