from django import forms
from landing.models import *


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        exclude = ['']
