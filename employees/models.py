from django.db import models
from enum import Enum

class Gender(Enum):
    M = "Male"
    F = "Female"

class Level(Enum):
    1 = "Bachelors Degree"
    2 = "Primary Education"

class education(models.Model):
    institution = models.CharField(max_length=200)
    level = models.CharField(max_length=1, choices=[(tag, tag.value) for tag in Level])
    specialization = models.CharField(max_length=200)
    grade = models.DecimalField(decimal_places=2, max_digits=3)
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(verbose_name="End Date")
    
class employee(models.Model):
    employee_number = models.CharField(max_length=10)
    first_name = models.Charfield(max_length=25)
    last_name = models.CharField(max_length=25)
    other_name = models.CharField(max_length=25)
    preferred_name = models.CharField(max_length=25)
    gender = models.CharField(max_length=5, choices=[(tag, tag.value) for tag in Gender ])
    dob = models.DateField(verbose_name="Date of Birth")
    work_email = models.EmailField()
    personal_email = models.EmailField()
    work_phone = models.PositiveIntegerField()
    personal_phone = models.PositiveIntegerField()
    twitter_url = models.URLField()
    facebook_url = models.URLField()
    linked_in = models.URLField()
    created_at = models.DateTimeField(auto_now=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)