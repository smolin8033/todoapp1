from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoItem
# Create your views here.

def todoView(request):
    return render(request, "todo.html", {})