from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from employee_app.models import Order
from employee_app.models import Meal
from datetime import datetime

def index(request):
    full_order_list = Order.objects.order_by('order_id')
    full_order_dict = {'Order': full_order_list}
    meal_list = Meal.objects.order_by('meal_id')
    meal1 = Meal.objects.get(meal_id=1)
    if request.method == 'POST':
        print(request.POST.get('number'))

        order=Order()
        order.order_number = request.POST.get('number')
        order.start_time = '2023-01-01 00:00'
        order.est_end_time = '2023-01-01 00:00'
        order.meal_id = meal1
        order.save()
        # return HttpResponseRedirect('')
    return render(request, 'employee_app/employee.html', context = full_order_dict)

