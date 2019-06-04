from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog


def home(request):
    contents = Blog.objects
    return render(request, 'home.html', {'contents': contents})
    # Blog Class로 부터 받은 모든 객체들을 contents, home에는 모든 contents를 띄워주니 사전형 객체 각 각 contents

def detail(request, id):
    details = get_object_or_404(Blog, pk = id)
    return render(request, 'detail.html', { 'content' : details}) 
    # details들, 보여주는 것들은 content에 하나하나 누를때마다 보여주는 것

def write(request):
    return render(request, 'write.html')
    # request가(html 파일 안 템플릿 태그 url 안의 write 누르면) 들어오면, write.html을 띄워라


def create(request): # 사용자가 write에 작성한 내용을 데이터베이스에 넣어주는 기능을 하는 함수
    newContent = Blog() #Blog()클래스에 새로운 인스턴스newContent
    newContent.title = request.GET['title']
    newContent.body = request.GET['body']
    newContent.pub_date = timezone.datetime.now()
    newContent.save() #.save() 쿼리셋 메소드 : 객체의 내용들을 데이터베이스에 저장해라
    return redirect('/blog/'+str(newContent.id)) # 새로운 컨텐트(인스턴스)의 생성된 아이디로 이동하라
