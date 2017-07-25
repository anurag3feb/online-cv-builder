from django.contrib import admin
from accounts.models import *
# Register your models here.

admin.site.register(PersonalDetails)
admin.site.register(SecondaryDetails)
admin.site.register(SeniorSecondaryDetails)
admin.site.register(GraduationDetails)
admin.site.register(Internship)
admin.site.register(Projects)
admin.site.register(Job)

