from rest_framework import permissions

class IsOwnerOrReadOnlyPublicPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.id is not None:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True

        if request.method in permissions.SAFE_METHODS:
            if obj.public == True:
                return True

        return False