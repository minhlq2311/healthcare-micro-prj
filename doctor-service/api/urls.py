# urls.py
from django.urls import path
from .views import DoctorDetail

urlpatterns = [
    path('doctor/<int:doctor_id>/', DoctorDetail.as_view()),
]