from django.db import models
from django.contrib.auth.models import AbstractUser

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Deal(models.Model):
    client = models.ForeignKey(Client, related_name='deals', on_delete=models.CASCADE)
    deal_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.client.name} - {self.amount}"
class CustomUser(AbstractUser):
    
    pass