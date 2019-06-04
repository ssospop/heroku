from django.shortcuts import render
from .models import Portfolio

def portfolio(request):
    contents = Portfolio.objects
    return render(request, 'portfolio.html', {'contents':contents})

