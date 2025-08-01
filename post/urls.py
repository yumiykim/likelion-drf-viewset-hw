from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from .views import PostViewSet, PostCommentViewSet

# 기본 Post 라우터
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')

# 댓글용 Nested 라우터
post_comment_router = NestedDefaultRouter(router, r'posts', lookup='post')
post_comment_router.register(r'comments', PostCommentViewSet, basename='post-comments')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(post_comment_router.urls)),
]
