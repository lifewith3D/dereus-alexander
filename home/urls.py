from django.urls import path
from . import views
from .views import UpdatePostView

urlpatterns = [
#     blogs
    path("", views.blogs, name="blogs"),
    path("archive", views.archive, name="archive"),
    path("blog/<str:slug>/", views.blogs_comments, name="blogs_comments"),
    path("edit_blog_post/<str:slug>/", UpdatePostView.as_view(), name="edit_blog_post"),
    path("delete_blog_post/<str:slug>/", views.Delete_Blog_Post, name="delete_blog_post"),
    path("search/", views.search, name="search"),
]