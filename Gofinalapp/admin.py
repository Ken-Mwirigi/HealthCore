from django.contrib import admin
from Gofinalapp.models import Members
from Gofinalapp.models import Product
from Gofinalapp.models import Appointment
from Gofinalapp.models import Contact
from Gofinalapp.models import User

# Register your models here.
admin.site.register(Members)
admin.site.register(Product)
admin.site.register(Appointment)
admin.site.register(Contact)
admin.site.register(User)