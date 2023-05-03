from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from employee_app.models import Order
from employee_app.models import Meal
from datetime import datetime
from .forms import MealForm

def index(request):
    form = MealForm


    full_order_list = Order.objects.order_by('order_id')
    full_order_dict = {'Order': full_order_list}
    meal_list = Meal.objects.order_by('meal_name')
    meal1 = Meal.objects.get(meal_name='MAC')
    if request.method == 'POST':
        # print(request.POST.get('number'))
        # print(request.POST.get('meal_name'))
        print(request.POST.get('meal_name'))
        selectedMeal = Meal.objects.get(meal_name=request.POST.get('meal_name').__str__())

        order=Order()
        order.order_number = request.POST.get('number')
        order.start_time = datetime.now.strftime("%Y-%m-%d %H:%M")
        order.est_end_time = '2023-01-01 00:00'
        order.meal = meal1
        order.save()

    return render(request, 'employee_app/employee.html', context = {'Order': full_order_list, 'Meal': meal_list, 'form':form})

