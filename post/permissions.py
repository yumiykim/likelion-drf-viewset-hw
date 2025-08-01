from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # 읽기는 누구나, 수정/삭제는 작성자만
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.writer == request.user or request.user.is_superuser
