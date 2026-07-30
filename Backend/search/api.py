from django.http import JsonResponse
from rest_framework.decorators import api_view
from Backend.post.models import Post
from Backend.post.models import Post
from Backend.post.serializers import PostSerializer
from account.models import User
from account.serializers import UserSerializer

@api_view(['GET'])
def search(request):
    data = request.data
    query = data.get('query', '')

    users = User.objects.filter(name__icontains=query)
    user_serializer = UserSerializer(users, many=True)

    posts = Post.objects.filter(body__icontains=query)
    post_serializer = PostSerializer(posts, many=True)

    return JsonResponse({
        'users': user_serializer.data,
        'posts': post_serializer.data
    }, safe=False)

