from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .import views
router=DefaultRouter()
router.register('contact_us',views.PatientViewSet)

urlpatterns=[
    path('',include(router.urls)),
    path('register/',views.UserRegistrationApiView.as_view(),name='register'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('logout/',views.UserLogOutView.as_view(),name='logout'),
    path('active/<uid64>/<token>',views.activate,name='activate'),
]
