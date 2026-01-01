from django.urls import path

from post.views import PostCreateView, PostDetailView

app_name = 'post'

urlpatterns = [
    # 게시글
    path('posts', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:post_id>', PostDetailView.as_view(), name='post-detail'),
    path("comments", PostCreateView.as_view(), name="comment-create")
]
