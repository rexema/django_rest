import io

from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.decorators import api_view, renderer_classes, action
from .models import Project, ToDo, User
from .serializers import ProjectSerializer, ToDoSerializer, UserSerializer, UserModelSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ProjectApiView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        project = Project.objects.all()
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def project_api_get(request):
    project = Project.objects.all()
    serializer = ProjectSerializer(project, many=True)
    return Response(serializer.data)


class ToDoViewSet(ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()


def user_get(request):
    user = User.objects.get(pk=2)
    serializer = UserModelSerializer(user)

    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data)


@csrf_exempt
def user_post(request, pk=None):
    json_data = JSONParser().parse(io.BytesIO(request.body))

    if request.method == 'POST':
        serializer = UserModelSerializer(data=json_data)
    elif request.method == 'PUT':
        user = User.objects.get(pk=pk)
        serializer = UserModelSerializer(user, data=json_data)
    elif request.method == 'PATCH':
        user = User.objects.get(pk=pk)
        serializer = UserModelSerializer(user, data=json_data, partial=True)

    if serializer.is_valid():
        user = serializer.save()

        serializer = UserModelSerializer(user)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data)

    return HttpResponseBadRequest(JSONRenderer().render(serializer.errors))
