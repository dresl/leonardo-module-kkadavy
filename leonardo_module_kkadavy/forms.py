# coding=utf-8
from __future__ import absolute_import

from crispy_forms.layout import HTML, Layout, Field, Fieldset, MultiField, Div
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.models import User
from django.contrib.auth.tokens import \
    default_token_generator as token_generator
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from horizon import forms, messages

from horizon.utils import validators
from horizon_contrib.forms import SelfHandlingForm
from leonardo.utils.emails import send_templated_email as send_mail
from django.conf import settings


class OrderForm(SelfHandlingForm):

    jmeno = forms.CharField(label=("Jméno"),
                            max_length=255,
                            widget=forms.TextInput(
        attrs={'placeholder':
               _('Username'),
               'autofocus': 'autofocus'}))

    prijmeni = forms.CharField(label=_("Prijmeni"),
                               max_length=255,
                               widget=forms.TextInput(
        attrs={'placeholder':
               _('Username'),
               'autofocus': 'autofocus'}))

    telefon = forms.IntegerField(label=_("Telefon"),
                                 widget=forms.NumberInput())

    email = forms.EmailField(label=_("E-mail"),
                             widget=forms.EmailInput())

    zprava = forms.CharField(label=_("Zprava"),
                             widget=forms.Textarea())

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)

        self.helper.layout = Layout(
            Div('jmeno', style='padding:0px', css_class='col-md-6'),
            Div('prijmeni', style='padding:0px', css_class='col-md-6'),
            Div('telefon', 'email', 'zprava', css_class='col-md-12')
        )

    def handle(self, request, data):
        if request.user.is_authenticated():
            messages.success(request, _("Order success."))
        else:
            messages.error(request, _("Login failed."))
        return True
