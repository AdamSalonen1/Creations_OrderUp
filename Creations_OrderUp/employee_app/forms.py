from django import forms
from django.forms import ModelForm
from .models import Meal, Login

class MealForm(ModelForm):
    class Meta:
        model = Meal
        fields = ('meal_id', 'meal_name')

class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = ('userid', 'username', 'password')