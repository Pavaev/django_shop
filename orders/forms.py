from django.forms import forms, CharField


class CheckoutContactForm(forms.Form):
    name = CharField(required=True)
    phone = CharField(required=True)


