from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    body = models.TextField()

    #Blog 객체 안의 제목을 객체로 만들어 주는 새로운 함수 
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
    