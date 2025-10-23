from django.contrib import admin
from .models import Feadback

# Register your models here.

class feadbackadmin(admin.ModelAdmin):
    list_display=('fead_doc','fead_dec')
admin.site.register(Feadback,feadbackadmin)