from django.db import models

# Create your models here.
class Patient(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField()
	medical_history = models.TextField()
	note = models.TextField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
 