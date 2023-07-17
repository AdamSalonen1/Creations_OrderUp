from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from employee_app.models import Order
from employee_app.models import Meal, Login
from mainApp import views
from datetime import datetime, timedelta
from .forms import MealForm
import time
from django.utils import timezone

authenticated = False
def index(request):

    try:
        cookie = request.COOKIES['authenticated']
    except:
        return redirect(login)

    if cookie != 'True':
        return redirect(login)

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
            if request.POST.get('Complete')=='Remove':
                complete_Order = Order.objects.get(order_id = request.POST.get('orders'))
                complete_Order.is_complete = True
                complete_Order.save()
                
                return HttpResponseRedirect('/employee?lastMeal={0}'.format(request.POST.get('meal').__str__()))
            
            else:
                selectedMeal = Meal.objects.get(meal_name=request.POST.get('meal_name').__str__())
                now = timezone.now()
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

def login(request):
    try:
        #when the cookie has already been added, the page is refreshed and we are brought back to the login which is wrong
        #we identify that the cookie is there and redirect back to the employee page
        cookie = request.COOKIES['authenticated']
        if cookie == 'True':
            return redirect(index)
    except:
        pass
    
    

    if request.method == 'POST':
        user = request.POST.get('username')
        password = request.POST.get('password')

        logins = Login.objects.all()

        for login in logins:
            if login.username == user and login.password == password:
                #because we have to return response, I made the response just refresh the page
                response = HttpResponse('<meta http-equiv=\"Refresh\" content=\"0; url=\'\" />')
                response.set_cookie('authenticated', 'True')
                return response


    return render(request, 'employee_app/login.html')