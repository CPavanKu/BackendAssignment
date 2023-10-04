# serializers.py
from rest_framework import serializers
from .models import User, Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

# views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import User, Post
from .serializers import UserSerializer, PostSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserLoginView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

# urls.py (in the api app)
from django.urls import path
from .views import UserCreateView, UserLoginView, PostCreateView

urlpatterns = [
    path('user/register/', UserCreateView.as_view(), name='user-register'),
    path('user/login/', UserLoginView.as_view(), name='user-login'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
]
