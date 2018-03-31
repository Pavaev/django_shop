from django.forms import forms, CharField


class CheckoutContactForm(forms.Form):
    email = CharField(required=True)
    phone = CharField(required=True)


