from django.contrib import admin

from .models import City,Event_Halls,Event_Hall_Availability,Reservation,Transaction

# Register your models here.

class CityAdmin(admin.ModelAdmin):
    model=City
    list_display = ['City_Name']

class EventHallAdmin(admin.ModelAdmin):
    model=Event_Halls
    list_display = ['City_Name','Hall_Name','Hall_Description','Hall_Guest_Capacity','Hall_Location','Slot','Price']

class AvailabiltyAdmin(admin.ModelAdmin):
    model=Event_Hall_Availability
    list_display = ['City_Name','Hall_Name','Availability_Start_Time','Availability_End_time']

class ReservationAdmin(admin.ModelAdmin):
    model=Reservation
    list_display = ['City_Name','Hall_Name','Customer_Name','Event_Date','Slot','Team_Size','Status']

class TransactionAdmin(admin.ModelAdmin):
    model=Transaction
    list_display = ['City_Name','Hall_Name']

admin.site.register(City,CityAdmin)
admin.site.register(Event_Halls,EventHallAdmin)
admin.site.register(Event_Hall_Availability,AvailabiltyAdmin)
admin.site.register(Reservation,ReservationAdmin)
admin.site.register(Transaction,TransactionAdmin)