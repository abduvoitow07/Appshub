from django.contrib import admin
from .models import Application


class ModelBook(admin.ModelAdmin):
    list_display = ('app', 'size', 'version', 'logo', 'file')
    search_fields = ('version', 'app')
    list_filter = ('size', 'version')


admin.site.register(Application, ModelBook)
