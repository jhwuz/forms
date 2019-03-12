from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phone_field import PhoneField


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Contact(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField()
    phone = PhoneField(blank=True)
    street = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=15)
    zipCode = models.CharField(max_length=5)
    message = models.TextField()
