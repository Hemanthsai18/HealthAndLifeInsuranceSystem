from django.contrib import admin
from .models import Health_Insurance,Life_Insurance,User_Own

# Register your models here.
admin.site.register(Health_Insurance)
admin.site.register(Life_Insurance)
admin.site.register(User_Own)