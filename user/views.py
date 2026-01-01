from django.http import JsonResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User


class SignUpView(APIView):
    """
    회원가입 API
    
    이메일과 비밀번호를 받아 새로운 사용자를 생성합니다.
    """

    @swagger_auto_schema(
        operation_summary="회원가입",
        operation_description="이메일과 비밀번호로 새로운 계정을 생성합니다.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['email', 'password'],
            properties={
                'email': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='사용자 이메일',
                    example='user@example.com'
                ),
                'password': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='비밀번호',
                    example='password123'
                ),
            }
        ),
        responses={
            201: openapi.Response(
                description="회원가입 성공",
                examples={
                    "application/json": {
                        "message": "회원가입 성공",
                        "user_id": 1,
                        "email": "user@example.com"
                    }
                }
            ),
            400: openapi.Response(
                description="잘못된 요청",
                examples={
                    "application/json": {
                        "error": "이메일과 비밀번호를 입력해주세요."
                    }
                }
            )
        },
        tags=['User']
    )
    def post(self, request):
        """회원가입 처리"""
        email = request.data.get('email')
        password = request.data.get('password')

        # 필수 입력 값 검증
        if not email or not password:
            return Response(
                {"error": "이메일과 비밀번호를 입력해주세요."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 이메일 중복 체크
        if User.objects.filter(email=email).exists():
            return Response(
                {"error": "이미 존재하는 이메일입니다."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 사용자 생성
        user = User.objects.create(
            email=email,
            password=password
        )

        return JsonResponse(
            {
                "message": "회원가입 성공",
                "user_id": user.id,
                "email": user.email
            },
            status=status.HTTP_201_CREATED
        )


class LoginView(APIView):
    """
    로그인 API
    
    이메일과 비밀번호로 사용자 인증을 수행합니다.
    """

    @swagger_auto_schema(
        operation_summary="로그인",
        operation_description="이메일과 비밀번호로 로그인합니다.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['email', 'password'],
            properties={
                'email': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='사용자 이메일',
                    example='user@example.com'
                ),
                'password': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='비밀번호',
                    example='password123'
                ),
            }
        ),
        responses={
            200: openapi.Response(
                description="로그인 성공",
                examples={
                    "application/json": {
                        "message": "로그인 성공",
                        "user_id": 1
                    }
                }
            ),
            400: openapi.Response(
                description="잘못된 요청",
                examples={
                    "application/json": {
                        "error": "이메일과 비밀번호를 입력해주세요."
                    }
                }
            ),
            401: openapi.Response(
                description="인증 실패",
                examples={
                    "application/json": {
                        "error": "이메일 또는 비밀번호가 올바르지 않습니다."
                    }
                }
            )
        },
        tags=['User']
    )
    def post(self, request):
        """로그인 처리"""
        email = request.data.get('email')
        password = request.data.get('password')

        # 필수 입력 값 검증
        if not email or not password:
            return Response(
                {"error": "이메일과 비밀번호를 입력해주세요."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 사용자 인증
        try:
            user = User.objects.get(email=email, password=password)

            return Response(
                {
                    "message": "로그인 성공",
                    "user_id": user.id
                },
                status=status.HTTP_200_OK
            )

        except User.DoesNotExist:
            return Response(
                {"error": "이메일 또는 비밀번호가 올바르지 않습니다."},
                status=status.HTTP_401_UNAUTHORIZED
            )
