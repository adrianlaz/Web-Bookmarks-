from rest_framework import serializers

from core.models import Bookmark
from django.contrib.auth.models import User


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'bookmarks']


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

        def save(self, validated_data):

            user = User.objects.create_user(validated_data['username'], None, validated_data['password'])

            return user


class PublicBookmarkSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Bookmark
        fields = ['id', 'title', 'url', 'owner', 'created_at']


class MyBookmarkSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Bookmark
        fields = ['id', 'title', 'url', 'public', 'owner', 'created_at']

    def create(self, validated_data):
        bookmark = Bookmark.objects.create(
            owner=self.context['request'].user,
            **validated_data
        )
        return bookmark
