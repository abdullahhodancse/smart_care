from django.shortcuts import render


from rest_framework import viewsets


from .import models
from .import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from rest_framework import filters


class doctorpagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerialaizers
    pagination_class=doctorpagination


class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerialaizers

class DesignationViewSet(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerialaizers

class AvaibleableTimeSpecificDoctor(filters.BaseFilterBackend):#particular doctor er availabe time ber kora
    def filter_queryset(self,request,query_set,view):
        doctor_id=request.query_params.get("doctor_id")
        if doctor_id:
            return query_set.filter(doctor = doctor_id)
        return query_set    


class AvailableTimeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerialaizers
    filter_backends=[AvaibleableTimeSpecificDoctor]



class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.review.objects.all()
    serializer_class = serializers.ReviewSerialaizers    