from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')], null=True)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)


class HealthRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blood_sugar = models.FloatField()
    date_recorded = models.DateField(auto_now_add=True)

class FoodCategory(models.Model):
    name = models.CharField(max_length=50)

class FoodMenu(models.Model):
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    suitable_for_diabetics = models.BooleanField(default=False)
