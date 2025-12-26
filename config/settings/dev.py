from dotenv import load_dotenv

from .base import *

env_path = os.path.join(BASE_DIR, "backend.env")
if os.path.exists(env_path):
    load_dotenv(env_path)

DEBUG = True
ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME', 'mydatabase'),
        'USER': os.getenv('DB_USER', 'sa'),
        'PASSWORD': os.getenv('DB_PASSWORD', '1234'),
        # 'HOST': os.getenv('DB_HOST', '127.0.0.1'),  # 백엔드 서버 로컬 환경 실행 시
        'HOST': os.getenv('DB_HOST', 'mysqldb'),  # 백엔드 서버 docker로 실행 시
        'PORT': int(os.getenv('DB_PORT', 3306)),
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}

CORS_ORIGIN_ALLOW_ALL = True
