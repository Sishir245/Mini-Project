from django.contrib import admin
from .models import Register, Appointment, Contact

# Register your models here.
admin.site.register(Register)
admin.site.register(Appointment)
admin.site.register(Contact)