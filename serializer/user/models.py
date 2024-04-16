from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(null= True)
    password=models.CharField(max_length=400)


    class Meta:
        db_table="user"
    




    

    

