from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from employee_app.models import Order
from employee_app.models import Meal
from datetime import datetime
from datetime import timedelta
from .forms import MealForm


def index(request):
    form = MealForm


    full_order_list = Order.objects.order_by('order_id')
    meal_list = Meal.objects.order_by('meal_name')
    if request.method == 'POST':        
        selectedMeal = Meal.objects.get(meal_name=request.POST.get('meal_name').__str__())
        now = datetime.now()
        order=Order()
        order.order_number = request.POST.get('number')
        order.start_time = now.strftime("%Y-%m-%d %H:%M")
        order.est_end_time = (now + timedelta(seconds=selectedMeal.cook_time)).strftime("%Y-%m-%d %H:%M")
        order.meal = selectedMeal
        order.save()

    return render(request, 'employee_app/employee.html', context = {'Order': full_order_list, 'Meal': meal_list, 'form':form})

