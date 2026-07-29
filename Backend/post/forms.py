from django.forms import ModelForm
from .models import Post, PostAttachment






class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['body',]