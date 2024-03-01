from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (AsideView, CommentView, FeedBackView, PostViewSet,
                    ProfileView, RegisterView, TagDetailView, TagView)

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path("", include(router.urls)),
    path("tags/", TagView.as_view()),
    path("aside/", AsideView.as_view()),
    path("tags/<slug:tag_slug>/", TagDetailView.as_view()),
    path("feedback/", FeedBackView.as_view()),
    path("register/", RegisterView.as_view()),
    path("profile/", ProfileView.as_view()),
    path("comments/", CommentView.as_view()),
    path("comments/<slug:post_slug>", CommentView.as_view()),

]
