from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home-page"),
    path("post", views.post, name="post-page"),
    path("post/<slug:slug>", views.post_detail, name="post-detail-page")
]
