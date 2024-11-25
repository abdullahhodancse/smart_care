from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient

# Create your models here.
class Specialization(models.Model):
    name=models.CharField(max_length=30)
    slug=models.SlugField(max_length=30)

    def __str__(self):
        return self.name 

class Designation(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50)

    def __str__(self):
        return self.name 


class AvailableTime(models.Model):
    name=models.CharField(max_length=100)


    def __str__(self):
        return self.name 

class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="doctor/images/")
    designation=models.ManyToManyField(Designation)
    speailaization=models.ManyToManyField(Specialization)
    availabletime=models.ManyToManyField(AvailableTime)
    Fee=models.IntegerField()
    Meet=models.CharField(max_length=150)


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
STAR_CHOICES=[
    ('★','★'),
   
   ( '★★','★★'),
    ('★★★','★★★'),
    ('★★★★','★★★★'),
    ('★★★★★','★★★★★'),
  
    
]        
class review(models.Model):
    reviwer=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    rating=models.CharField(max_length=10 ,choices=STAR_CHOICES)

    def __str__(self):
        return f"Paitent:{self.reviwer.user.first_name};Doctor:{self.doctor.user.first_name}"

