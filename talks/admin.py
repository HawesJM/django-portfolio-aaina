from django.contrib import admin
from .models import Talk

class TalkAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'recorded_date',
        'url',
    )
    ordering = ('recorded_date',)

admin.site.register(Talk, TalkAdmin)
