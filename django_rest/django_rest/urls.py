"""django_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from todo.views import *
from todo.serializers import *
from users import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
import users.urls
from users.views import UserListApiView
from users.serializers import UserSerializerUpdate
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = DefaultRouter()

schema_view = get_schema_view(
    openapi.Info(
        title='todo',
        default_version='v1',
        description='Documentation',
        contact=openapi.Contact(email='nastya@mail.ru'),
        license=openapi.License(name='MIT LICENSE'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],

)

router.register('users', CustomUserViewSet)
router.register('project', ProjectViewSet)
router.register('todo', ToDoViewSet)
router.register('user_list', UserViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('user_get/<int:pk>', user_get),
    path('user_get/', user_get),
    path('user_post', user_post),
    path('user_post/<int:pk>', user_post),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token/',obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('users.urls')),
    # path('swagger<str:format>/', schema_view.with_ui()),
    # path('swagger/', schema_view.with_ui('swagger')),
    path('redoc/', schema_view.with_ui('redoc')),

]
