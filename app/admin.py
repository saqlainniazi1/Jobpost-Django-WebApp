from django.contrib import admin

from app.models import JobPost, Location, Author, Skills


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'salary', 'description')
    list_filter = ('date', 'salary')
    search_fields = ('title', 'date',)
    search_help_text = 'search title and date'
    # fields = (('title', 'description'), 'salary')
    # exclude = ('title',)
    # fieldsets = (
    #     ('Basic information', {
    #         'fields': ('title', 'description')
    #     }),
    #     ('More information', {
    #         'classes': ('collapse', 'wide'),
    #         'fields': (('salary', 'expiry'), 'slug')
    #     }),
    #
    # )


# Register your models here.

admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills)
