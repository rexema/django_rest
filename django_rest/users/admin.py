from django.contrib import admin

from django.contrib import admin
from .models import CustomUser


class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'username',
        'email'
    ]
admin.site.register(CustomUser, UserAdmin)
