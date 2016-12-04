from django.conf.urls import patterns, url
from django.views.generic import RedirectView

from . import views

urlpatterns = patterns(
    "",
    url(r"^order_sth/$", views.OrderSthView.as_view(), name="order_sth"),
)
