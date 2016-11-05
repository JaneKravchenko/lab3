from django.contrib import admin

# Register your models here.
from .models import Measurment, Area_inform, Areas

admin.site.register(Measurment)
admin.site.register(Areas)
admin.site.register(Area_inform)