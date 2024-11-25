from django.db import models
from doctor.models import Doctor,AvailableTime
from patient.models import Patient

# Create your models here.
Appointment_status=[
    ('Completed','Completed'),
    ('Running','Running'),
    ('Pending','Pending'),
    

]
Appoinment_Types=[
    ('Offline','Offline'),
    ('Online','Online'),
]
class Appointment(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    appoinment_type=models.CharField(max_length=20,choices=Appoinment_Types,)
    appointment_status=models.CharField(max_length=20,choices=Appointment_status,default="Pending")
    symtoms=models.TextField()
    time=models.ForeignKey(AvailableTime,on_delete=models.CASCADE)
    cancel=models.BooleanField(default=False)

    def __str__(self):
        return f"Doctor:{self.doctor.user.first_name}, Patient:{self.patient.user.first_name}"

    

