from django.db import models

# Create your models here.
#Schema -structure of database

class Student(models.Model):
   # id =models.AutoField()
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.TextField(null= True,blank =True)

    """def __str__(self)->str:
        return self.name
"""


class Car(models.Model):
    car_name=models.CharField(max_length=20)
    speed=models.IntegerField(default=50)


    def __str__(self)->str:
        return self.car_name


    
    