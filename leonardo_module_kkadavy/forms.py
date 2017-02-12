# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.utils import timezone

from crispy_forms.layout import \
    HTML, Layout, Field, Fieldset, MultiField, Div
from crispy_forms.bootstrap import PrependedText
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.models import User
from django.contrib.auth.tokens import \
    default_token_generator as token_generator
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from horizon import forms, messages

from .models import Orders

from horizon.utils import validators
from horizon_contrib.forms import SelfHandlingForm
from leonardo.utils.emails import send_templated_email as send_mail
from django.conf import settings


class OrderForm(SelfHandlingForm):

    import sys
    reload(sys)
    sys.setdefaultencoding('UTF8')

    error_required = 'Toto pole je vyžadováno.'
    invalid_email_message = 'Zadejte správný formát e-mailu.'

    jmeno = forms.CharField(label="Jméno",
                            max_length=255,
                            widget=forms.TextInput(
                                attrs={'placeholder':
                                       'Jméno',
                                       'autofocus': 'autofocus'}),
                            error_messages={'required': error_required})

    prijmeni = forms.CharField(label="Příjmení",
                               max_length=255,
                               widget=forms.TextInput(
                                   attrs={'placeholder':
                                          'Příjmení'}),
                               error_messages={'required': error_required})

    email = forms.EmailField(label="E-mail",
                             widget=forms.EmailInput(
                                 attrs={'placeholder': 'E-mail'}),
                             error_messages={'required': error_required,
                                             'invalid': invalid_email_message})

    telefon = forms.IntegerField(label="Telefon",
                                 widget=forms.NumberInput(
                                     attrs={'placeholder': 'Telefon'}),
                                 error_messages={'required': error_required})

    zprava = forms.CharField(label="Zpráva",
                             widget=forms.Textarea(
                                 attrs={
                                     'placeholder':
                                     'Zašlete nám Vaši objednávku'}),
                             error_messages={
                                 'required': error_required
                             })

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)

        self.helper.layout = Layout(
            Div('jmeno', style='padding:5px', css_class='col-md-6'),
            Div('prijmeni', style='padding:5px', css_class='col-md-6'),
            PrependedText('email', '@', placeholder="E-mail"),
            Div('telefon', 'zprava', style='padding:5px',
                css_class='col-md-12')
        )

    def handle(self, request, data):
        Orders.objects.create(jmeno=data['jmeno'],
                              prijmeni=data['prijmeni'],
                              email=data['email'],
                              telefon=data['telefon'],
                              zprava=data['zprava'],
                              datum=timezone.now())
        messages.success(request, "Objednávka úspěšně dokončena.")
        return True


class SendMessageForm(SelfHandlingForm):

    import sys
    reload(sys)
    sys.setdefaultencoding('UTF8')

    error_required = 'Toto pole je vyžadováno.'

    zprava = forms.CharField(label="Vzkaz",
                             widget=forms.Textarea(
                                 attrs={
                                     'placeholder':
                                     'Podpořte Jitku'}),
                             error_messages={
                                 'required': error_required
                             },
                             help_text="Tento vzkaz se zobrazí na hlavní stránce")

    def __init__(self, *args, **kwargs):
        super(SendMessageForm, self).__init__(*args, **kwargs)

        self.helper.layout = Layout(
            Div('zprava', style='padding:5px',
                css_class='col-md-12')
        )

    def handle(self, request, data):
        order = Orders.objects.create(jmeno=timezone.now().year +
                              timezone.now().month + timezone.now().day,
                              prijmeni=str(timezone.now(
                              ).year) + " " +
                              str(timezone.now().month) + "." + str(timezone.now().day),
                              email=" ",
                              telefon=0,
                              zprava=data['zprava'],
                              datum=timezone.now())
        order.save()
        messages.success(request, "Vzkaz úspěšne poslán.")
        return True
