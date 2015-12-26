
from django.contrib import admin
from details.models import Employee,Address,Skills
admin.autodiscover()

admin.site.register(Employee)
admin.site.register(Address)
admin.site.register(Skills)