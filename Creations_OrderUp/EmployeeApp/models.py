from django.db import models


class Order(models.Model):
    orderId = models.BigAutoField(primary_key=True)
    orderNumber = models.IntegerField()
    startTime = models.DateTimeField(auto_now=True)
    endTime = models.DateTimeField()
    isComplete = models.BooleanField(auto_created=False)

    def __str__(self):
        return self.orderNumber.__str__()

class MealType(models.Model):
    mealId = models.BigAutoField(primary_key=True)
    mealName = models.CharField(max_length=255)
    mealPrepTime = models.FloatField()

    def __str__(self):
        return self.mealName