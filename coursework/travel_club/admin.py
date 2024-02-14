from django.contrib import admin
from .models import (Amateur, Sportsman, Coach, Section, Administration, Manager, Group, Event, Competition,
                     Training, Instructor, Place, Route, Tour)


admin.site.register([Sportsman, Section, Administration, Manager, Group, Event, Competition,
                     Training, Instructor, Place, Route, Tour])


class AmateurAdmin(admin.ModelAdmin):
    fields_for_list = [field.name for field in Amateur._meta.get_fields() if not field.is_relation]
    list_display = fields_for_list
    # list_display = ('first_name', 'last_name')


admin.site.register(Amateur, AmateurAdmin)

class CoachAdmin(admin.ModelAdmin):
    fields_for_list = [field.name for field in Coach._meta.get_fields() if not field.is_relation]
    list_display = fields_for_list

admin.site.register(Coach, CoachAdmin)