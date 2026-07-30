from django.shortcuts import render
from django.http import JsonResponse

from Backend.account.models import User
from Backend.account.serializers import UserSerializer

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



@api_view(['GET'])
def post_list_profile(request, id):
    user = User.objects.get(pk=id)
    posts = Post.objects.filter(created_by_id=id)
    post_serializer = PostSerializer(posts, many=True)
    user_serializer = UserSerializer(user)
    return JsonResponse({
        'user': user_serializer.data,
        'posts': post_serializer.data
    }, safe=False)


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
    


    
