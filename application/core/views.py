from django.contrib.auth.models import User

from rest_framework import viewsets, permissions, mixins

from core.models import Bookmark
from core.serializers import CreateUserSerializer, PublicBookmarkSerializer, MyBookmarkSerializer


class CreateUserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer


class PublicBookmarkViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = PublicBookmarkSerializer

    def get_queryset(self):
        return Bookmark.objects.all().filter(public=True)


class MyBookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = MyBookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)

