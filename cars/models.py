from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


# Create your models here.
class CustomCars(models.Model):
    class Meta:
        db_table = 'auth_cars'

    brand = models.CharField(max_length=20)
    year = models.IntegerField()
    speed = models.IntegerField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='cars')
