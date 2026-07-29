from .models import Post, PostAttachment
from rest_framework import serializers
from account.serializers import UserSerializer



class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'





