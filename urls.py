# api/urls.py
from django.urls import path
from .views import UserCreateView, UserLoginView, PostCreateView

urlpatterns = [
    path('user/register/', UserCreateView.as_view(), name='user-register'),
    path('user/login/', UserLoginView.as_view(), name='user-login'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
]


# BackendAssignment/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include the app-specific URLs here
]
