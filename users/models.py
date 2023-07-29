from django.db import models

# Create your models here.



class User(models.Model):
    GENDER=(
        ('Male','Male'),
            ('Female','Female')
            )
    

    f_name = models.CharField(max_length=200,null=True)
    l_name = models.CharField(max_length=200,null=True)
    gender=models.CharField(max_length=20,null=True,choices=GENDER)
    phone = models.CharField(max_length=10,null=True)
    email = models.EmailField(null=True)
    password =models.CharField(max_length=50,null=True)


    def __str__(self):
        return (str(self.f_name) if self.f_name else "") + " " + (str(self.l_name) if self.l_name else "")
    






