from django.db import models
from django.utils.crypto import get_random_string
class ContactEntry(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    
class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    verification_code = models.CharField(max_length=50, blank=True, null=True)
    # Add other fields as needed

    def generate_verification_code(self):
        return get_random_string(length=32)

