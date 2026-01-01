from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from post.models import Post
from post.serializers import PostCreateSerializer, PostDetailViewSerializer, CommentSerializer


class PostCreateView(APIView):
    """
    게시글 생성 API
    
    user_id, title, content를 받아 새로운 게시글을 생성합니다.
    """
    
    @swagger_auto_schema(
        operation_summary="게시글 생성",
        operation_description="새로운 게시글을 작성합니다.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['user_id', 'title', 'content'],
            properties={
                'user_id': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description='작성자 ID',
                    example=1
                ),
                'title': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='게시글 제목',
                    example='첫 번째 게시글'
                ),
                'content': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='게시글 내용',
                    example='게시글 내용입니다.'
                ),
            }
        ),
        responses={
            201: openapi.Response(
                description="게시글 생성 성공",
                examples={
                    "application/json": {
                        "id": 1,
                        "user_id": 1,
                        "title": "첫 번째 게시글",
                        "content": "게시글 내용입니다.",
                        "created_at": "2025-01-01T10:00:00Z",
                        "updated_at": "2025-01-01T10:00:00Z"
                    }
                }
            ),
            400: openapi.Response(
                description="잘못된 요청",
                examples={
                    "application/json": {
                        "error": "user_id를 입력해주세요."
                    }
                }
            )
        },
        tags=['Post']
    )
    def post(self, request):
        """게시글 생성 처리"""
        user_id = request.data.get('user_id')

        # 필수 입력 값 검증
        if not user_id:
            return Response(
                {"error": "user_id를 입력해주세요."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Serializer를 통한 유효성 검증 및 저장
        serializer = PostCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(APIView):
    """
    게시글 상세 조회 API
    
    게시글 ID로 특정 게시글의 상세 정보를 조회합니다.
    """
    
    @swagger_auto_schema(
        operation_summary="게시글 상세 조회",
        operation_description="특정 게시글의 상세 정보를 조회합니다.",
        manual_parameters=[
            openapi.Parameter(
                'post_id',
                openapi.IN_PATH,
                description="게시글 ID",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        responses={
            200: openapi.Response(
                description="조회 성공",
                examples={
                    "application/json": {
                        "id": 1,
                        "user_id": 1,
                        "title": "첫 번째 게시글",
                        "content": "게시글 내용입니다.",
                        "created_at": "2025-01-01T10:00:00Z",
                        "updated_at": "2025-01-01T10:00:00Z"
                    }
                }
            ),
            404: openapi.Response(
                description="게시글을 찾을 수 없음",
                examples={
                    "application/json": {
                        "error": "게시글을 찾을 수 없습니다."
                    }
                }
            )
        },
        tags=['Post']
    )
    def get(self, request, post_id):
        """게시글 상세 조회 처리 (댓글 포함)"""
        try:
            # 게시글 조회
            post = Post.objects.get(id=post_id)

            # Serializer를 통한 응답 데이터 생성
            serializer = PostDetailViewSerializer(post)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Post.DoesNotExist:
            return Response(
                {"error": "게시글을 찾을 수 없습니다."},
                status=status.HTTP_404_NOT_FOUND
            )


class CommentCreateView(APIView):
    """
    댓글 생성 API
    
    user_id, post_id, content를 받아 게시글에 댓글을 작성합니다.
    """
    
    @swagger_auto_schema(
        operation_summary="댓글 생성",
        operation_description="특정 게시글에 댓글을 작성합니다.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['user_id', 'post', 'content'],
            properties={
                'user_id': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description='작성자 ID',
                    example=1
                ),
                'post': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description='게시글 ID',
                    example=1
                ),
                'content': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='댓글 내용',
                    example='좋은 글이네요!'
                ),
            }
        ),
        responses={
            201: openapi.Response(
                description="댓글 생성 성공",
                examples={
                    "application/json": {
                        "id": 1,
                        "post": 1,
                        "user_id": 1,
                        "content": "좋은 글이네요!",
                        "created_at": "2025-01-01T10:00:00Z",
                        "updated_at": "2025-01-01T10:00:00Z"
                    }
                }
            ),
            400: openapi.Response(
                description="잘못된 요청",
                examples={
                    "application/json": {
                        "error": "user_id와 post_id를 입력해주세요."
                    }
                }
            )
        },
        tags=['Post']
    )
    def post(self, request):
        """댓글 생성 처리"""
        user_id = request.data.get('user_id')
        post_id = request.data.get('post')

        # 필수 입력 값 검증
        if not user_id or not post_id:
            return Response(
                {"error": "user_id와 post_id를 입력해주세요."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Serializer를 통한 유효성 검증 및 저장
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
