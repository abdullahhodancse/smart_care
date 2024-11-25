from rest_framework import serializers
from . import models

class DoctorSerialaizers(serializers.ModelSerializer):
   user = serializers.StringRelatedField(many=False)
   designation = serializers.StringRelatedField(many=True)
   speailaization = serializers.StringRelatedField(many=True)
   availabletime= serializers.StringRelatedField(many=True)
  

   class Meta:
        model=models.Doctor
        fields='__all__'


class SpecializationSerialaizers(serializers.ModelSerializer):
   
   class Meta:
        model=models.Specialization
        fields='__all__'

class DesignationSerialaizers(serializers.ModelSerializer):
  
   class Meta:
        model=models.Designation
        fields='__all__'    

class AvailableTimeSerialaizers(serializers.ModelSerializer):
   
   class Meta:
        model=models.AvailableTime
        fields='__all__'


class ReviewSerialaizers(serializers.ModelSerializer):
   
   class Meta:
        model=models.review
        fields='__all__'