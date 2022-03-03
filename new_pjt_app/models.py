from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class skill_table(models.Model):
    skills = models.CharField(max_length=100)
    
    def _str_(self):
        return self.skills

class first_model(models.Model):
    id=models.AutoField(primary_key=True)
    user_Name = models.CharField(max_length=50)
    user_Address = models.CharField(max_length=100)
    user_Age = models.IntegerField()
    Date_Of_birth = models.DateField()
    skills = models.ForeignKey(skill_table, on_delete=models.CASCADE, default=True, null=False )
    
    def _str_(self):
        return self.skills





