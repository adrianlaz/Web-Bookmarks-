from django.urls import path, include
from rest_framework.routers import SimpleRouter

from core import views

router = SimpleRouter()

router.register(r'create-user', views.CreateUserViewSet)
router.register(r'public-bookmarks', views.PublicBookmarkViewSet)
router.register(r'my-bookmarks', views.MyBookmarkViewSet)


urlpatterns = [
    path('', include(router.urls)),
]