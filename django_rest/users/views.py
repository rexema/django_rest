import io

from django.http import HttpResponse,HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet
from .models import CustomUser
from .serializers import CustomUserModelSerializer,CustomUserSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class CustomUserModelViewSet(ModelViewSet):
    serializer_class = CustomUserModelSerializer
    queryset = CustomUser.objects.all()


def user_get(request, pk=None):
    if pk is not None:
        user = CustomUser.objects.get(pk=pk)
        serializer = CustomUserSerializer(user)

    else:
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)

    json_data = JSONRenderer().render(serializer.data)
    #print(serializer.data)
    return HttpResponse(json_data)
@csrf_exempt
def user_post(request):
    json_data = JSONParser().parse(io.BytesIO(request.body))

    if request.method == 'POST':
        serializer = CustomUserSerializer(data=json_data)
    elif request.method == 'PUT':
        user = CustomUser.objects.get(pk=5)
        serializer = CustomUserSerializer(user, data=json_data)
    elif request.method == 'PATCH':
        user = CustomUser.objects.get(pk=5)
        serializer = CustomUserSerializer(user, data=json_data, partial=True)

    if serializer.is_valid():
        user = serializer.save()

        serializer = CustomUserSerializer(user)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data)

    return HttpResponseBadRequest(JSONRenderer().render(serializer.errors))


