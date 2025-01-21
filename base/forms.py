from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Project, Post

class ProjectAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Project
        fields = '__all__'

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = '__all__'
