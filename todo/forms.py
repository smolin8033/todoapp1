from django import forms
from .models import TodoItem

class TodoItemForm(forms.ModelForm):
    content = forms.CharField

    class Meta:
        model = TodoItem
        fields = [
            "content",
        ]