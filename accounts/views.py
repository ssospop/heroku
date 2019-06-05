from django.shortcuts import render, redirect
#밑 두개는 장고에서 제공하는 기능, 복붙용, 계정 관련
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method =="POST": #회원 가입 후 form 제출 버튼 누르면, POST로 제출 되었다면
        if request.POST['password1'] == request.POST['password2']:
            if User.objects.filter(username=request.POST['username']).exists():
                return render(request,'signup.html', {'already':'이미 가입한 아이디 입니다'})
            else:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1']) #아이디를 만들어주는 함수를 그대로 쓰면 됨
                auth.login(request, user) #회원가입 후 자동 로그인
                return redirect('home') # 위의 함수를 다 실행 후 띄워줄 화면, home에 해당하는 url로 이동
    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password'] #login.html의 name =password , signup과 다름
        user = auth.authenticate(request, username=username, password=password) # 실제 회원 명단에 있는지 확인하는 함수
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method =="POST":
        auth.logout(request)
        return redirect('home')
    return render(request, 'login.html') #else생략된것 # login안한 상태면 그냥 login.html 실행되게

# Create your views here.
