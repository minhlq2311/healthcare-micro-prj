import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Appointment
from .serializers import AppointmentSerializer

class MakeAppointment(APIView):
    def post(self, request):
        data = request.data
        patient_id = data.get("patient_id")
        doctor_id = data.get("doctor_id")

        # Gọi nội bộ
        patient_response = requests.get(f"http://patient-service:8000/patient-service/record/{patient_id}/")

        if patient_response.status_code != 200:
            return Response({"error": "Invalid patient"}, status=400)

        doctor_response = requests.get(f"http://doctor-service:8000/doctor-service/doctor/{doctor_id}/")
        if doctor_response.status_code != 200:
            return Response({"error": "Invalid doctor"}, status=400)

        appointment = Appointment.objects.create(
            patient_id=patient_id,
            doctor_id=doctor_id,
            date=data.get("date")
        )
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data, status=201)
