from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = (
        ("student", "Student"),
        ("admin", "Admin"),
        ("tutor", "Tutor"),
        ("worker", "Worker")
    )
    
    role = models.CharField(max_length=50, choices=ROLE_CHOICES,default="student")
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ["username"]
    USERNAME_FIELD = "email"
    
    def __str__(self):
        return f"{self.email}"
    
    
    
    
    
    
