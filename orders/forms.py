from django.forms import forms, CharField, IntegerField


class CheckoutContactForm(forms.Form):
    name = CharField(required=True)
    phone = CharField(required=True)


class BasketPanelForm(forms.Form):
    count = IntegerField(min_value=1, required=True)
