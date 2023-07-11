from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from datetime import datetime
from employee_app.models import Order
import json


def index(request):

    #this makes it so that if there is an order that is complete for more than 3 minutes it will disappear
    myOrders = Order.objects.filter(is_complete=False)
    for o in myOrders:
        now = datetime.now()
        difference = now.replace(tzinfo=None) - o.est_end_time.replace(tzinfo=None)

        #for whatever reason when the difference is negative it shoots the number up to like 86,000 so we just make it fall within a range
        if difference.seconds > 180 and difference.seconds < 80000:
            o.is_complete = True           
            o.save()


    full_order_list = Order.objects.filter(is_complete=False)

    if request.method == 'POST':
        print("posting")
        json_data = json.loads(request.body.decode('utf-8'))
        order = Order.objects.get(order_id=json_data['order_id'])

        order.is_complete = True
        order.save(force_update=True)

        full_order_list = Order.objects.filter(is_complete=False)

        print('line before httpresponse redirect')

        print('printing ads', request.POST.get('ads'))
        if request.POST.get('ads') == 1:
            print('got ads post')
            return HttpResponseRedirect('advertisements/')

        return render(request, 'mainApp/index.html', context={'Order': full_order_list})
    

        


    return render(request, 'mainApp/index.html', context={'Order': full_order_list})


def advertisements(request):
    full_order_list = Order.objects.filter(is_complete=False)
    
    return render(request, 'mainApp/advertisements.html', context={'Order': full_order_list})
