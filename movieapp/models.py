from sqlite3 import SQLITE_CONSTRAINT_NOTNULL
from django.db import models

# Create your models here.
class Censorinfo(models.Model):
    rating=models.CharField(max_length=10)
    Certifiedby=models.CharField(max_length=30)
    def __str__(self):
        return self.Certifiedby
    
class Movieinfo(models.Model):
    Title=models.CharField(max_length=250)
    Year=models.IntegerField(null=False)
    summary=models.TextField()
    success=models.TextField(default="no data")
    #poster=models.ImageField(upload_to='images/',null=True)
    #censordetails=models.OneToOneField(Censorinfo,null=True)
    def __str__(self):
        return self.Title

class Director(models.Model):
    Name=models.CharField(max_length=20)
    def __str__(self):
        return self.Name

    