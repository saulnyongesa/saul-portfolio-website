from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

class User(AbstractUser):
    # Added validation and metadata
    name = models.CharField(max_length=100, null=True, verbose_name="Full Name")
    
class Project(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name="Project Name")
    description = models.TextField(null=True, verbose_name="Project Description")
    photo = models.ImageField(upload_to='projects/', null=True, verbose_name="Project Photo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    
    def __str__(self):
        return self.name

class Email(models.Model):
    email = models.EmailField(max_length=254, null=True, verbose_name="Email Address")
    subject = models.CharField(max_length=100, null=True, verbose_name="Email Subject")
    message = models.TextField(null=True, verbose_name="Email Message")
    sent_at = models.DateTimeField(default=now, verbose_name="Sent At")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    
    def __str__(self):
        return self.email

class Skill(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name="Skill Name")
    description = models.TextField(null=True, verbose_name="Skill Description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    
    def __str__(self):
        return self.name

