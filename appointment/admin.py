from django.contrib import admin
from .import models
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display=['id','doctor_name','patient_name','appoinment_type','appointment_status','symtoms','time','cancel']
    

    def doctor_name(self,obj):
        return obj.doctor.user.first_name


    def patient_name(self,obj):
        return obj.patient.user.first_name 

    def save_model(self,request,obj,form,change):
        obj.save()
        if obj. appointment_status=="Running" and obj.appoinment_type=="Online":
            email_subject="Appointment"
            email_body=render_to_string('appointment_email.html',{'user':obj.patient.user,'doctor':
            obj.doctor
            
            })
            email=EmailMultiAlternatives(email_subject,'',to=[obj.patient.user.email])
            email.attach_alternative(email_body,"text/html")
            email.send()
                


admin.site.register(models.Appointment,AppointmentAdmin)
