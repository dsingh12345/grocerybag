from django.db import models

# Create your models here.
class grocerylist(models.Model):
    name = models.CharField(max_length = 75)
    itemquantity = models.CharField(max_length = 75)
    status = models.IntegerField()
    date = models.DateField( max_length=50)
    def __str__(self):
        return self.name
    
class login(models.Model):
    name = models.CharField(max_length = 75)
    password = models.CharField(max_length = 75)
     
    def __str__(self):
        return self.name
    
