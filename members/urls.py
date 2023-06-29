from django.urls import path
from .views import home, posts, details, post_creation, searchresult_home, searchresult_posts

urlpatterns = [
    path("", home, name="home"),
    path("home/", home, name="home"),
    path("posts/<slug>/", posts, name="posts"),
    path("details/<slug>/", details, name="details"),
    path("post_creation/", post_creation, name="post_creation"),
    path("searchresult_home/", searchresult_home, name="searchresult_home"), 
    path("searchresult_posts/", searchresult_posts, name="searchresult_posts"),
]
