
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from .models import Blog,BlogComment

class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())  # Correctly set CKEditorWidget for content

    class Meta:
        model = Blog  # Reference the Blog model
        fields = '__all__'  # Include all fields in the form

class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm  # Use the custom form for the admin

admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment)
