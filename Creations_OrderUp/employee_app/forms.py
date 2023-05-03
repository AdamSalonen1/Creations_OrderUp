from django import forms
from django.forms import ModelForm
from .models import Meal

class MealForm(ModelForm):
    class Meta:
        model = Meal
        fields = ('meal_id', 'meal_name')