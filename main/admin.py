from django.contrib import admin
# Register your models here.
import os
import glob
from .models import *


@admin.register(Subdomain)
class SubdomainAdmin(admin.ModelAdmin):
    list_display = ['sub_domain', 'status','created']
    model = Subdomain
    def response_change(self, request, obj):
        ret = super().response_change(request, obj)
        if '_Delete' in request.POST:
            print("-----delete---------")
            files = glob.glob('D:/django/test/*')
            for f in files:
                os.remove(f)
        return ret