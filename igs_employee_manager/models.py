from django.db import models


class Collaborators(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(null=False)
    phone_number = models.IntegerField(null=False)
    salary = models.FloatField()
    
    
class Departments(models.Model):
    name = models.CharField(max_length=30)
    budget = models.FloatField()
    responsible = models.ForeignKey(Collaborators, on_delete=models.CASCADE)