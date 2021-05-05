from django.contrib import admin
from .models import Building, Appartment, Visitor, Mainentance_Header, Mainentance_Line, Mainentance_pays

# Register your models here.

Models = (Building, 
Appartment,
Visitor,
Mainentance_Header,
Mainentance_Line,
Mainentance_pays)

admin.site.register(Models)