from django.contrib import admin
# Register your models here.
import os
from .models import *


@admin.register(Subdomain)
class SubdomainAdmin(admin.ModelAdmin):
    list_display = ['sub_domain', 'status','created']
    model = Subdomain
    def delete_model(self, request, obj):
        print('==========================delete_model==========================')
        print(obj)
        os.remove("/tmp/hx.txt")
        obj.delete()
        print('==========================delete_model==========================')
    

