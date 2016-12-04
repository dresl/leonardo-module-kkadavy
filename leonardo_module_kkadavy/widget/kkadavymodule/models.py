# -#- coding: utf-8 -#-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from leonardo.module.web.models import Widget
from leonardo_module_kkadavy.models import Orders


class KkadavyModuleWidget(Widget):

    class Meta:
        abstract = True
        verbose_name = _('Kkadavy module')
        verbose_name_plural = _('Kkadavy modules')
