
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

default_app_config = 'leonardo_module_kkadavy.Config'


class Default(object):

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
    verbose_name = _("KkadavyModule")


default = Default()
