from django.contrib import admin

from folders.models import Folder


class FolderInline(admin.TabularInline):
    model = Folder
    readonly_fields = ['path']
    show_change_link = True


class FolderAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (('name', 'parent'), 'path')
        }),
    )
    inlines = [FolderInline]
    list_display = ['path', 'parent']
    raw_id_fields = ['parent']
    readonly_fields = ['path']
    search_fields = ['name', 'path']



admin.site.register(Folder, FolderAdmin)
