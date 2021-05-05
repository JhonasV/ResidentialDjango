from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Building(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name
    

class Appartment(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    number = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.name

class Visitor(models.Model):
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    name = models.CharField(max_length=30)
    appartment = models.ForeignKey(Appartment, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Mainentance_Header(models.Model):
    total_cost = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return selg.total_cost


class Mainentance_Line(models.Model):
    mainentance_header = models.ForeignKey(Mainentance_Header, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.description


class Mainentance_pays(models.Model):
    mainentance_header = models.ForeignKey(Mainentance_Header, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    appartment = models.ForeignKey(Appartment, on_delete=models.CASCADE)

    def __str__(self):
        return self.mainentance_header.total_cost
    