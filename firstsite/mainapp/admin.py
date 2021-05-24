from django.contrib import admin
from .models import About, Address, Atmosfere, Services

admin.site.register(Services)

admin.site.register(About)

admin.site.register(Atmosfere)

admin.site.register(Address)

# admin.site.register(Phone_number)