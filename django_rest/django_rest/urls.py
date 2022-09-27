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
from rest_framework.routers import DefaultRouter

from todo.views import *

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('project', ProjectViewSet)
router.register('todo', ToDoViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('user_get/<int:pk>', user_get),
    path('user_get/', user_get),
    path('user_post', user_post),
    path('user_post/<int:pk>', user_post),
    path('project_api_get', project_api_get),
    path('project_api_get_class', ProjectApiView.as_view()),

]
