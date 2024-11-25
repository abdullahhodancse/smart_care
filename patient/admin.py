from django.contrib import admin
from .models import Patient

# Register your models here.
class Patientadmin(admin.ModelAdmin):
    list_display=['id','last_name','first_name','Mobile_number','image']



    def first_name(self,obj):
        return obj.user.first_name

    def last_name(self,obj):
        return obj.user.last_name     



admin.site.register(Patient,Patientadmin)
