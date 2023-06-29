from django import forms
from django.forms import ModelForm
from .models import Post, Category

class PostForm(ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = Post
        fields = ["title", "content", "categories", "tags"]