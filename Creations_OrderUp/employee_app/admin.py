from django.contrib import admin
from employee_app.models import Order
from employee_app.models import Meal, Login
# Register your models here.

admin.site.register(Order)
admin.site.register(Meal)
admin.site.register(Login)