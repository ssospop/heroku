from django.urls import path
from . import views
#accounts 안에 있는 urls.py는 프로젝트폴더 안 url의 첫번째 admin부분은 왜 임포트 안해줘도 되는가?

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name="logout"), #logout.html은 만들필요 없지만 urls는 해줘야 views를 실행 할 수 있음
]