from django.db import models

# Create your models here.

class Building(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name