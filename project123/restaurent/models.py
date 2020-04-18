from django.db import models
from s_admin.models import AreaOperations,Restrotype

class RegistrationFrom(models.Model):
    no = models.AutoField(primary_key=True)
    restro_name = models.CharField(max_length=30,unique=True)
    restro_contact = models.IntegerField()
    restro_email = models.EmailField()
    restro_area = models.ForeignKey(AreaOperations,on_delete=models.CASCADE)
    restro_type = models.ForeignKey(Restrotype,on_delete=models.CASCADE)
    restro_password = models.CharField(max_length=30)
    otp = models.IntegerField()
    restro_status = models.CharField(max_length=30, default=False)




