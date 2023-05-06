from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from employee_app.models import Order
import json

def index(request):
    full_order_list = Order.objects.filter(is_complete = False)

    if request.method == 'POST':    
        print("posting")  
        json_data = json.loads(request.body.decode('utf-8'))
        order = Order.objects.get(order_id = json_data['order_id'])
        
        order.is_complete = True
        order.save(force_update=True)

        full_order_list = Order.objects.filter(is_complete = False)

        print('line before httpresponse redirect')
        return render(request, 'mainApp/index.html', context = {'Order':full_order_list})
    

    return render(request, 'mainApp/index.html', context = {'Order':full_order_list})
    
           

def advertisements(request):
    full_order_list = Order.objects.filter(is_complete = False)
    return render(request, 'mainApp/advertisements.html', context = {'Order':full_order_list})