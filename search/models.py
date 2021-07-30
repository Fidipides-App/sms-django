from django.db import models
from django.utils.translation import ugettext_lazy as _


class Pacient(models.Model):
    name = models.CharField(max_length=255, blank=True, verbose_name=_("Name"))
    code = models.IntegerField(unique=True, verbose_name=_("Code"))
    phone = models.CharField(max_length=15, unique=True, blank=False, verbose_name=_("Phone Number"))
    email = models.EmailField(unique=True, blank=True, verbose_name=_("Email Address"))
    address = models.TextField(max_length=255, blank=True, verbose_name=_("Address"))
    city = models.CharField(max_length=50, blank=True, verbose_name=_("City"))
    postal_code = models.CharField(max_length=8, blank=True, verbose_name=_("Postal Code"))
    notes = models.TextField(max_length=255, blank=True, verbose_name=_("Notes"))
    birthdate = models.DateField(blank=True, verbose_name=_("Birth Date"))

    class Meta:
        verbose_name = _("Pacient")
        verbose_name_plural = _("Pacients")

    def __str__(self):
        return self.name
