from django.contrib import admin

from search.models import Pacient


@admin.register(Pacient)
class PacientAdmin(admin.ModelAdmin):
    pass
