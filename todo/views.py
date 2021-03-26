from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TodoItem
from .forms import TodoItemForm
# Create your views here.

def todoView(request):
    queryset = TodoItem.objects.all()
    context = {
        "object_list": queryset,
    }
    return render(request, "todo.html", context)

def createView(request):
    form = TodoItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/todo/")
    context = {
        "form": form,
    }
    return render(request, "todo.html", context)