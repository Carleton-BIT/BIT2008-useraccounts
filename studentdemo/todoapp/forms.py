from django import forms
from .models import Task, CustomUser
from django.contrib.auth.forms import UserCreationForm


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description']


class CustomUserCreationForm(UserCreationForm):
    is_omniscient = forms.BooleanField(required=False, label="Register as omniscient user")

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('is_omniscient',)