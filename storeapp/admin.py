from django.contrib import admin
from .models import Contact
from .models import FormSubmission

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')


class FormSubmissionAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'dob', 'age', 'gender', 'phone', 'email', 'department', 'course', 'purpose', 'materials')

admin.site.register(Contact, ContactAdmin)
admin.site.register(FormSubmission, FormSubmissionAdmin)
