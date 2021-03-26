from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoItem
# Create your views here.

def todoView(request):
    queryset = TodoItem.objects.all()
    context = {
        "object_list": queryset,
    }
    return render(request, "todo.html", context)