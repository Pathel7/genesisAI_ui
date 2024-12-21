from django.contrib import admin
from .models import Contact



class AdminCont(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')


admin.site.register(Contact, AdminCont)
