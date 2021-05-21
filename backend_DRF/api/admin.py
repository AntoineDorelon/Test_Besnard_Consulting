from django.contrib import admin
from .models import AgilePrinciples, AgileValues
# admin name and password is 'root'

admin.site.register(AgilePrinciples)
admin.site.register(AgileValues)
