from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path,include

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]