from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class City(models.Model):
    City_Name = models.CharField(max_length=50,blank=False, null=False, default=' ')

    def __str__(self):
        return self.City_Name

class Event_Halls(models.Model):
    City_Name = models.ForeignKey(City, on_delete=models.CASCADE)
    Hall_Name = models.CharField(max_length=50, default=' ', null=True, blank=True)
    Hall_Description = models.CharField(max_length=50, default=' ', null=True, blank=True)
    Hall_Guest_Capacity = models.IntegerField(blank=True, null=True)
    Hall_Location= models.CharField(max_length=50,default='',)
    Slot= models.CharField(max_length=50, default='4 hours', null=True, blank=True)
    Price = models.IntegerField(blank=True, null=True)
    #Hall_Image=models.ImageField(upload_to='Images',default='Images/pool.jpg')

    def __str__(self):
        return self.Hall_Name

class Event_Hall_Availability(models.Model):
    City_Name = models.ForeignKey(City, on_delete=models.CASCADE)
    Hall_Name = models.ForeignKey(Event_Halls, on_delete=models.CASCADE)
    Availability_Start_Time = models.DateTimeField(blank=True, null=True)
    Availability_End_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.Hall_Name.Hall_Name

class Reservation(models.Model):
    City_Name = models.ForeignKey(City, on_delete=models.CASCADE)
    Hall_Name = models.ForeignKey(Event_Halls, on_delete=models.CASCADE)
    Customer_Name = models.CharField(max_length=50, default=' ', null=True, blank=True) #Changed to charfield. change back to foriegnkey
    Event_Date = models.DateTimeField(blank=True, null=True)
    TIMEPERIOD= [ ('8.00 - 12.00','8.00 - 12.00'),('12.00 - 4.00','12.00 - 4.00'),('4.00 - 8.00','4.00 - 8.00'),('8.00','12.00'),]
    Slot = models.CharField(max_length=50, choices=TIMEPERIOD)
    SIZE = [ (1, '10'),(2, '20'),(3, '30'),(4, '40'),(5, '50'),(6, '60'),(7, '70'),(8, '80'), (9, '90'),
        (10, '100'),]
    Team_Size = models.CharField(max_length=50, default=' ', null=True, blank=True)
    Status = models.CharField(max_length=50, default=' ', null=True, blank=True)


    def __str__(self):
        return self.Hall_Name.Hall_Name

class Transaction(models.Model):
    City_Name = models.ForeignKey(City, on_delete=models.CASCADE)
    Hall_Name = models.ForeignKey(Event_Halls, on_delete=models.CASCADE)
    Customer_Name = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    Trans_Amount = models.CharField(max_length=50, default=' ', null=True, blank=True)
    Trans_Time_Date = models.DateTimeField(blank=True, null=True)
    Trans_Type = models.CharField(max_length=50, default=' ', null=True, blank=True)
    Transaction_Token = models.CharField(max_length=50, default=' ', null=True, blank=True)

    def __str__(self):
        return self.Trans_Amount