from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class  User(AbstractUser):
    address = models.CharField(max_length=200,null=True,blank="True")
   



class Company(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

plantype = (
    ('MONTHLY','MONTHLY'),
    ('YEARLY','YEARLY')
)

class Plan(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True, null=True,blank=True )
    update_at = models.DateTimeField(auto_now=True, null=True,blank=True )
    plantype = models.CharField(max_length=200,choices=plantype)
    Company = models.ForeignKey(to=Company, on_delete=models.CASCADE, related_name="Plan_company",null=True,blank=True)
    
    def __str__(self):
        return self.name
    


    


class UserPlans(models.Model):
    ActivePlan = models.DateTimeField(auto_now=True, null=True,blank=True )
    PlanExpire = models.DateTimeField(null=True,blank=True )
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="userplan_user",null=True,blank=True)
    plan = models.ForeignKey(to=Plan, on_delete=models.CASCADE, related_name="Userplan_plan",null=True,blank=True)


    
   
   
    










