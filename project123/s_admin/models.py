from django.db import models

class LoginModel(models.Model):
    username = models.CharField(primary_key=True,max_length=30)
    password = models.CharField(max_length=30)
    OTP = models.IntegerField()

class StateModel(models.Model):
    sno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=30,unique=True)
    def __str__(self):
        return self.sname

class CityModel(models.Model):
    cno = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=30)
    state = models.ForeignKey(StateModel,on_delete=models.CASCADE)
    def __str__(self):
        return self.cname
class AreaOperations(models.Model):
    ano = models.AutoField(primary_key=True)
    area_name = models.CharField(max_length=30)
    city = models.ForeignKey(CityModel,on_delete=models.CASCADE)
    def __str__(self):
        return self.area_name

class Restrotype(models.Model):
    resno = models.AutoField(primary_key=True)
    restype = models.CharField(max_length=30,unique=True)
    def __str__(self):
        return self.restype

