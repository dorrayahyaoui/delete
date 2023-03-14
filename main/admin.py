from django.contrib import admin
# Register your models here.
import os
from .models import *


@admin.register(Subdomain)
class SubdomainAdmin(admin.ModelAdmin):
    list_display = ['sub_domain', 'status','created']
    model = Subdomain
    def response_change(self, request, obj):
        ret = super().response_change(request, obj)
        if '_Delete' in request.POST:
            print("-----delete---------")
            os.remove("C:/Users/g700515/Desktop/fluv")
        return ret