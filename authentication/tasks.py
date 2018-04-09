import logging

from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from my_shop.celery import app




@app.task
def send_verification_email(user_id):
    User = get_user_model()
    try:
        user = User.objects.get(id=user_id)
        print(user)
        send_mail(
            'Verify your QuickPublisher account',
            'Follow this link to verify your account: '
            'http://localhost:8000%s' % reverse('auth:verify', kwargs={'uuid': str(user.verification_uuid)}),
            'panaev.smtp@gmail.com',
            [user.email],
            fail_silently=False,
        )
    except User.DoesNotExist:
        logging.warning("Tried to send verification email to non-existing user '%s'" % user_id)