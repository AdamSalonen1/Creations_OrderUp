from django.shortcuts import render
from django.http import HttpResponse
from employee_app.models import Order

def index(request):
    full_order_list = Order.objects.order_by('order_id')
    full_order_dict = {'Order': full_order_list}
    return render(request, 'mainApp/index.html', context = full_order_dict)


def advertisements(request):
    return render(request, 'mainApp/advertisements.html')