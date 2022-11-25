from django.urls import path
from .views import UserListApiView


app_name = 'users'

urlpatterns = [
    path('api/<str:version>/users/', UserListApiView.as_view()),
]