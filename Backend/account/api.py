from django.http import JsonResponse

from rest_framework.decorators import api_view,authentication_classes , permission_classes

from account.serializers import UserSerializer , FriendshipRequestSerializer

from .forms import SignUpForm
from .models import User,FriendshipRequest




@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    message = 'success'


    form = SignUpForm({

        'email': data.get('email'),
        'name': data.get('name'),   
        'password1': data.get('password1'),
        'password2': data.get('password2'),




   } )

    if form.is_valid():
        form.save()


    else:
        message = 'error'
        # sending verification email logic here


    return JsonResponse({'status':message})


@api_view(['POST'])
def friends(request,pk):
    user = User.objects.get(pk=pk)
    requests = []
    u=request.user
    u.friends_count = 1
    user.save()




    if user == request.user:
        requests = FriendshipRequest.objects.filter(created_for=user, status=FriendshipRequest.SENT)
        requests = FriendshipRequestSerializer(requests, many=True).data

    friends = user.friends.all()  

    return JsonResponse({
        'user': UserSerializer(user).data,
        'friends': UserSerializer(friends, many=True).data,
        'requests': FriendshipRequestSerializer(requests, many=True).data
    }, safe=False)  


@api_view(['POST'])
def send_friendship_request(request,pk):
    user = User.objects.get(pk=pk)

    check1 = FriendshipRequest.objects.filter(created_by=request.user, created_for=user)
    check2 = FriendshipRequest.objects.filter(created_by=user, created_for=request.user)

    if not check1.exists() and not check2.exists():
        friendship_request = FriendshipRequest.objects.create(created_by=request.user, created_for=user)
        return JsonResponse({'status':'success','message':'Friendship request sent successfully.'})
    else:
        return JsonResponse({'status':'error','message':'Friendship request already sent.'})



@api_view(['POST'])
def handle_request(request,pk,status):
    user = User.objects.get(pk=pk)
    friendship_request = FriendshipRequest.objects.get(created_by=user, created_for=request.user)


    if status == 'accept':
        friendship_request.created_by.friends.add(friendship_request.created_for)
        friendship_request.created_for.friends.add(friendship_request.created_by)
        friendship_request.created_by.friends_count += 1
        friendship_request.created_for.friends_count += 1
        friendship_request.delete()
        return JsonResponse({'status':'success','message':'Friendship request accepted.'})
    elif status == 'reject':
        friendship_request.delete()
        friendship_request.created_by.friends_count -= 1
        friendship_request.created_for.friends_count -= 1
        return JsonResponse({'status':'success','message':'Friendship request rejected.'})
    else:
        return JsonResponse({'status':'error','message':'Invalid status.'})
