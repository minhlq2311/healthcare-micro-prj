from django.urls import path
from .views import DoctorDetail, DoctorList

urlpatterns = [
    path('doctor/<int:doctor_id>/', DoctorDetail.as_view()),
    path('doctors/', DoctorList.as_view()),
]
