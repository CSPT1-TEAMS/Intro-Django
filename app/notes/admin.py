from django.contrib import admin

from .models import Note, PersonalNote


class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    readonly_fields = ("created_at", "last_modified")


class PersonalNoteAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "author")
    readonly_fields = ("created_at", "last_modified")


admin.site.register(Note, NoteAdmin)
admin.site.register(PersonalNote, PersonalNoteAdmin)

