from django.shortcuts import render
from django.http import HttpResponse
from employee_app.models import Order
from employee_app.models import Meal

def index(request):
    full_order_list = Order.objects.order_by('order_id')
    full_order_dict = {'Order': full_order_list}
    meal_list = Meal.objects.order_by('meal_id')
    if request.method == 'POST':
        if request.POST.get('number'):
            order=Order()
            order.order_number = request.POST.get('number')
            order.save()
    return render(request, 'employee_app/employee.html', context = full_order_dict)

