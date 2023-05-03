from django.db import models
from django.utils.translation import gettext_lazy as _
   
# Note: Meals are children of Orders. Meals can be thouht of as the actual dish that is served for an Order.


class Meal(models.Model):
    class MealType(models.TextChoices):
        # [examples, need to fill]
        MAC_AND_CHEESE = "MAC", _("Mac and Cheese")
        PIZZA = "PIZ", _("Pizza")
        PASTA = "PAS", _("Pasta")
    
    # Fields
    meal_id = models.BigAutoField(primary_key=True)
    meal_name = models.CharField(
        max_length=3,
        choices=MealType.choices,
    )
    cook_time = models.DateTimeField()

    def __str__ (self):
        return self.meal_id
    
    # Note: meal_name field has two parts, value and human-readable value. A method for human readable value is auto created by django
    # E.g. A meal is created with name "meal" as a Meal object with meal_name = MAC 
    # meal.meal_name >>> 'MAC'
    # meal.get_meal_name_display() >>> 'Mac and Cheese'

class Order(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    order_number = models.IntegerField()
    start_time = models.DateTimeField(auto_now=True)
    est_end_time = models.DateTimeField()
    is_complete = models.BooleanField(default=False)
    meal_id = models.ForeignKey(Meal, on_delete=models.CASCADE)

    def __str__ (self):
        return self.order_id