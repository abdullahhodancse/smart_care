from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .import views
router=DefaultRouter()
router.register('Doctor',views.DoctorViewSet)
router.register('Specialization',views.SpecializationViewSet)
router.register('Designation',views.DesignationViewSet)
router.register('AvailableTime',views.AvailableTimeViewSet)
router.register('Review',views.ReviewViewSet)


urlpatterns=[
    path('',include(router.urls)),
]