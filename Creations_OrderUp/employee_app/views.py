from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from employee_app.models import Order
from employee_app.models import Meal
from datetime import datetime
from datetime import timedelta
from .forms import MealForm


def index(request):
    lastMeal = '---------'
    hasError = False
    if 'hasError' in request.GET:
        hasError = True

    try:
        if 'lastMeal' in request.GET:
            lastMeal = request.GET.get('lastMeal').__str__()

        form = MealForm(initial={'meal_name' : lastMeal})

        full_order_list = Order.objects.filter(is_complete = False)
        meal_list = Meal.objects.order_by('meal_name')

        if request.method == 'POST': 
            print(request.POST.get('orders'))
            if request.POST.get('Complete')=='Complete':
                print("thank god")
                complete_Order = Order.objects.get(order_number = request.POST.get('orders'))
                print("got complete order")
                complete_Order.is_complete = True
                print("iscomplete = true")
                complete_Order.save()
                print("order saved")
                return HttpResponseRedirect('/employee?lastMeal={0}'.format(request.POST.get('meal').__str__()))
            
            else:
                print("NOOOOOOO")
                selectedMeal = Meal.objects.get(meal_name=request.POST.get('meal_name').__str__())
                now = datetime.now()
                order=Order()
                order.order_number = request.POST.get('number')
                order.start_time = now.strftime("%Y-%m-%d %H:%M:%S")
                order.est_end_time = (now + timedelta(seconds=selectedMeal.cook_time)).strftime("%Y-%m-%d %H:%M:%S")
                order.meal = selectedMeal
                order.save()
                return HttpResponseRedirect('/employee?lastMeal={0}'.format(request.POST.get('meal_name').__str__()))
    except:
        return HttpResponseRedirect('/employee?hasError=True')

    return render(request, 'employee_app/employee.html', context = {'Order': full_order_list, 'Meal': meal_list, 'form':form, 
                                                                    'hasError':hasError})

