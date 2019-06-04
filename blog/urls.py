from django.contrib import admin
from django.urls import path
# import blog.views를 지금은 blog라는 폴더 안에 있으니까 밑으로 수정 가능
from . import views

urlpatterns = [
    path('<int:id>', views.detail, name="detail"),
    path('write', views.write, name="write"),
    path('create', views.create, name="create"),
]