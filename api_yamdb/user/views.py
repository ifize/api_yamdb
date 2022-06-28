from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from user.models import User
from user.serializers import UserSerializer, UserEditSerializer
from api.permissions import IsAdmin


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdmin,)
    lookup_field = 'username'

    @action(methods=['GET', 'PATCH'],
            url_path='me',
            serializer_class=UserEditSerializer,
            permission_classes=[permissions.IsAuthenticated],
            detail=False)
    def profile(self, request):
        user = request.user
        if request.method == 'GET':
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if request.method == 'PATCH':
            serializer = self.get_serializer(
                user,
                data=request.data,
                partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
