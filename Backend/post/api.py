from django.shortcuts import render
from django.http import JsonResponse

from .models import Post
from . serializers import PostSerializer
from rest_framework.decorators import api_view

# Create your views here.



@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)


    return JsonResponse(serializer.data, safe=False)

    
