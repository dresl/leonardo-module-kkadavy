# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth import logout as auth_logout
from django.contrib.sites.models import Site
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from leonardo import forms, messages

from .forms import OrderForm, SendMessageForm
from django.http import HttpResponseRedirect
from leonardo.decorators import require_auth

from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator


class OrderSthView(forms.ModalFormView):
    form_class = OrderForm
    template_name = 'leonardo_kkadavy/order_sth.html'
    submit_label = _("Objednat")

    def get_context_data(self, **kwargs):
        ret = super(OrderSthView, self).get_context_data(**kwargs)

        ret.update({
            "view_name": 'Objednávací list',
            "modal_size": 'md',
            "modal_header": 'Objednávací list'})

        return ret


class SendMessageView(forms.ModalFormView):
    form_class = SendMessageForm
    template_name = 'leonardo_kkadavy/send_sth.html'
    submit_label = _("Poslat")

    def get_context_data(self, **kwargs):
        attr = super(SendMessageView, self).get_context_data(**kwargs)

        attr.update({
            "view_name": 'Vzkaz',
            "modal_size": 'md',
            "modal_header": 'Pošlete vzkaz'})

        return attr
