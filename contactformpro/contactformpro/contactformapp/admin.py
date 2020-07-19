from django.contrib import admin

from .models import ContactData

class AdminContactData(admin.ModelAdmin):
    list_display = ['name','mobile','email','location','course']


admin.site.register(ContactData,AdminContactData)