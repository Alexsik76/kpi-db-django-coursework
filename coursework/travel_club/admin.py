from django.contrib import admin
from .models import (Amateur, Sportsman, Coach, Section, Administration, Manager, Group, Event, Competition,
                     Training, Instructor, Place, Route, Tour, Person, Tourist)


admin.site.register([Sportsman, Administration, Manager, Event, Competition,
                     Training, Instructor, Place, Route, Tour, Person])


class AmateurAdmin(admin.ModelAdmin):
    fields_for_list = ['first_name', 'last_name', 'group',]
    print(fields_for_list)
    list_display = fields_for_list


admin.site.register(Amateur, AmateurAdmin)


class TouristAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'section_name']

    @admin.display(ordering="section_name", description="Section name")
    def section_name(self, obj):
        if obj.group:
            return f"{obj.group.section.name}"


admin.site.register(Tourist, TouristAdmin)


class CoachAdmin(admin.ModelAdmin):
    fields_for_list = [field.name for field in Coach._meta.get_fields() if not field.is_relation]
    list_display = fields_for_list


admin.site.register(Coach, CoachAdmin)


class GroupAdmin(admin.ModelAdmin):
    list_display = ['section_name', 'coach_name',]

    @admin.display(ordering="section_name", description="Section name")
    def section_name(self, obj):
        if obj.section:
            return f"{obj.section.name}"

    @admin.display(ordering="coach_name", description="Coach name")
    def coach_name(self, obj):
        if obj.coach:
            return f"{obj.coach.first_name} {obj.coach.last_name}"


admin.site.register(Group, GroupAdmin)


class SectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']



admin.site.register(Section, SectionAdmin)
