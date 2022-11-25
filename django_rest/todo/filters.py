from django_filters import rest_framework as filters
from .models import *

class UserFilter(filters.FilterSet):
    first_name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model=User
        fields=['first_name']


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model=Project
        fields=['name']


class ToDoFilter(filters.FilterSet):
    date_of_creation = filters.DateFromToRangeFilter()

    class Meta:
        model = ToDo
        fields = ['date_of_creation']