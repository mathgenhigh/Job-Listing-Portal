from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('job_seeker', 'Job Seeker'),
        ('employer', 'Employer')
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    
    @property
    def profile(self):
        from jobs.models import Profile 
        profile, created = Profile.objects.get_or_create(user=self)
        return profile
    
    def __str__(self):
        return f"{self.username} ({self.role})"
