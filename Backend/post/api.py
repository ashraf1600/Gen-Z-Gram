from django.shortcuts import render
from django.http import JsonResponse

from .models import Post
from . serializers import PostSerializer
from rest_framework.decorators import api_view
from . forms import PostForm

# Create your views here.



@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)


    return JsonResponse(serializer.data, safe=False)




@api_view(['POST'])
def post_create(request):
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        post = form.save(commit=False)
        post.created_by = request.user
        post.save()
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data, status=201)
    else:
        return JsonResponse(form.errors, status=400)
    


    
