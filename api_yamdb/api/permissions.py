from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_admin or request.user.is_superuser)


class IsAuthorOrReadOnlyPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user
            or request.method in permissions.SAFE_METHODS
        )


class IsAdminOrReadOnlyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and request.user.is_admin
            or request.method in permissions.SAFE_METHODS
        )


# class IsAuthenticatedOrReadOnlyPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return (
#             request.user.is_authenticated
#             or request.method in permissions.SAFE_METHODS
#         )

#     def has_object_permission(self, request, view, obj):
#         return (
#             request.user.is_authenticated and (
#                 obj.author == request.user
#                 or request.user.is_admin
#             )
#         )


class OnlyReadOrСhangeAuthorAdminModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_admin
            or request.user.is_moderator
            or obj.author == request.user)
