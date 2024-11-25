from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from .import models
from .import serializers

class AppoinmentViewSet(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppoinmentSerialaizers


    # custom query kora 
    def get_queryset(self):
        queryset=super().get_queryset() #kahini holo "queryset = models.Appointment.objects.all()" k inherit korlam
        patient_id=self.request.query_params.get('patient_id')#user er deya patient_id k niya aslam
        if patient_id:
            queryset=queryset.filter(patient_id=patient_id)
        return queryset    



# def get_queryset(self):
#     queryset = super().get_queryset()  # Inherits the default queryset
#     patient_id = self.request.query_params.get('patient_id')  # Retrieve patient_id from query parameters
#     if patient_id:
#         try:
#             patient_id = int(patient_id)  # Convert to integer if necessary
#             queryset = queryset.filter(patient_id=patient_id)  # Filter the queryset
#         except ValueError:
#             # Handle invalid patient_id gracefully, e.g., return an empty queryset or raise an error
#             queryset = queryset.none()
#     return queryset



