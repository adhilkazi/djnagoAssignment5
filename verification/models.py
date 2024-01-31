from django.db import models

class vfn(models.Model):
      firstname=models.CharField(max_length=200,null=True)
      lastname=models.CharField(max_length=200,null=True)
      email=models.CharField(max_length=200,null=True)
      phone=models.IntegerField(null=True)                                           
      password=models.CharField(max_length=200,null=True)
      conform_password=models.CharField(max_length=200,null=True)
      gender=models.CharField(max_length=200,null=True)
    