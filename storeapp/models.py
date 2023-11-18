from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name


class FormSubmission(models.Model):
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    department = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    purpose = models.CharField(max_length=50)
    materials = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Form Submission - {self.username}"