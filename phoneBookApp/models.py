from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Number(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='numbers')
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.number 