from django.contrib import admin
from .models import Task, CustomUser
from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.register(Task)
admin.site.register(CustomUser, UserAdmin)