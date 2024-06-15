# forms.py
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','author','headings','image','content']
        widgets = {
            'content': CKEditorWidget(),
        }




