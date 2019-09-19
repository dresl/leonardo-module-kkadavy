# -#- coding: utf-8 -#-
from django.db import models
from django.conf import settings
from django.utils import timezone


class Orders(models.Model):

    jmeno = models.CharField(max_length=255, verbose_name="Jméno", default=' ')
    prijmeni = models.CharField(
        max_length=255, verbose_name="Příjmení", default=' ')
    email = models.EmailField(verbose_name="E-mail", default=' ')
    telefon = models.PositiveIntegerField(
        verbose_name="Telefon", default=0)
    zprava = models.TextField(verbose_name="Zpráva", default=' ')
    datum = models.DateTimeField(
        verbose_name="Datum objednávky", default=timezone.now())

    def __unicode__(self):
        return self.jmeno

    class Meta:
        ordering = ['jmeno', ]
        verbose_name = 'Položka'
        verbose_name_plural = 'Položky'
