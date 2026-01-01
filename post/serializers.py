from rest_framework import serializers

from .models import Post, Comment


class PostCreateSerializer(serializers.ModelSerializer):
    """게시글 생성 Serializer"""

    class Meta:
        model = Post
        fields = ['id', 'user_id', 'title', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class PostDetailViewSerializer(serializers.ModelSerializer):
    "게시글 상세 조회용 Serializer(댓글 포함)"

    class Meta:
        model = Post
        fields = ['id', 'user_id', 'title', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    "댓글 생성 Serializer"

    class Meta:
        model = Comment
        fields = ['id', 'post', 'user_id', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
