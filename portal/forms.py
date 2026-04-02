from django import forms
from .models import Reminder, feedback
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['task', 'date']

class feedbackForm(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ['mood', 'note']

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']