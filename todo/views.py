from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoItemForm
# Create your views here.

def todoView(request):
    form = TodoItemForm(request.POST or None)
    queryset = TodoItem.objects.all()
    context = {
        "object_list": queryset,
        "form": form,
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

def deleteView(request):
    pass