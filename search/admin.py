from django.contrib import admin

from search.models import Patient


@admin.register(Patient)
class PacientAdmin(admin.ModelAdmin):
    pass
