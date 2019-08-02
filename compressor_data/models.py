from django.db import models
from django.utils import timezone
# Create your models here.
from iot_data import settings


class User_Detail(models.Model):
    company_name=models.CharField(max_length=30)
    user_name_1=models.CharField(max_length=30)
    user1_mobile=models.CharField(max_length=10)
    user_name_2 = models.CharField(max_length=30)
    user2_mobile=models.CharField(max_length=10)
    user_name_3 = models.CharField(max_length=30)
    user3_mobile=models.CharField(max_length=10)
    dealer_name = models.CharField(max_length=30)
    dealer1_mobile=models.CharField(max_length=10)
    dealer2_mobile=models.CharField(max_length=10)
    craeted_date_and_time=models.DateTimeField(default=timezone.now())

class Compressor_data(models.Model):
    company=models.ForeignKey(User_Detail,on_delete=models.CASCADE)
    compressor_serial_number=models.CharField(max_length=30)
    model=models.CharField(max_length=30)
    type=models.CharField(max_length=30)
    year_of_purchase=models.CharField(max_length=12)
    anydesk_num=models.CharField(max_length=30)
    total_running_hrs=models.CharField(max_length=7)
    change_fule_in=models.CharField(max_length=7)
    maintance_in=models.CharField(max_length=7)
