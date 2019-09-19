# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

default_app_config = 'leonardo_module_kkadavy.Config'

try:
    from local_settings import APPS
except ImportError:
    pass

class Default(object):
    if 'leonardo_module_kkadavy' in APPS:
        optgroup = 'Kkadavy widgets'

        apps = [
            'leonardo_module_kkadavy'
        ]

        widgets = [
            'leonardo_module_kkadavy.widget.kkadavymodule.models.KkadavyModuleWidget'
        ]

        public = True


class Config(AppConfig, Default):
    name = 'leonardo_module_kkadavy'
    verbose_name = "Speciální modul"


default = Default()
