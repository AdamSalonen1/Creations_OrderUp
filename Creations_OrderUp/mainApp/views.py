from django.shortcuts import render
from django.http import HttpResponse
from employee_app.models import Order
import json

def index(request):
    full_order_list = Order.objects.order_by('order_id')
    full_order_dict = {'Order': full_order_list}
    if request.method == 'POST':
        json_data = json.loads(request.body.decode('utf-8'))
        order = Order.objects.get(order_id = json_data['order_id'])
        
        print(json_data['order_id'])
        order
        order.is_complete = True
        print(order.est_end_time)
        order.save()
        
    return render(request, 'mainApp/index.html', context = full_order_dict)


def advertisements(request):
    return render(request, 'mainApp/advertisements.html')