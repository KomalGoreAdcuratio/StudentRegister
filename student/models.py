from django.db import models

# Create your models here.
class StudentRegistration(models.Model):
    email = models.EmailField(max_length=50,primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    password = models.CharField(max_length=100, default="", null=False)
    gender = (
    ("M","Male"),
    ("F","Female"),
    )
    gender = models.CharField(max_length=1, choices=gender, default="M",    null=False)
    school = models.CharField(max_length=50, default="N/A")