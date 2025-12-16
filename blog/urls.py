from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.post_list, name="list"),
    path("post/<int:pk>/", views.post_detail, name="detail"),
    path("post/new/", views.post_create, name="create"),
    path("post/<int:pk>/edit/", views.post_edit, name="edit"),
    path("post/<int:pk>/like/", views.post_like, name="like"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
]


