from django.contrib import admin
from bboard.models import Bb, Rubric


@admin.register(Bb)
class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'published')
    list_filter = ['title', 'published', 'rubric' ]
    search_fields = ['title']
    date_hierarchy = 'published'
    ordering = ['published']



admin.site.register(Rubric)
# Register your models here.
