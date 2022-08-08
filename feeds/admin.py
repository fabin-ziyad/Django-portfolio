from django.contrib import admin
from .models import *

#######################################################################################################
# EXTRA CLASS
class PersonalInformationAdmin(admin.ModelAdmin):
    list_display = ('name_complete', 'address')
    search_fields = ["name_complete"]
class Myvalues(admin.ModelAdmin):
    list_display=('Full_Name','Email','Subject','Messages')
    search_fields=['Full_Name','Email','Subject','Messages']

#######################################################################################################
# REGISTER MODELS
admin.site.register(PersonalInformation,PersonalInformationAdmin)
admin.site.register(About)
admin.site.register(RecentWork)
admin.site.register(Allwork)
admin.site.register(Skill_Language)
admin.site.register(MyModel,Myvalues)

#######################################################################################################
