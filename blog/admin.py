from django.contrib import admin
from .models import Blog # models.py에 있는 Blog 객체 import

admin.site.register(Blog)
