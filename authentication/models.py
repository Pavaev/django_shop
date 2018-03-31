import uuid

from django.core.mail import send_mail, EmailMessage
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Permission
from django.db.models import signals
from django.urls import reverse

from my_shop import settings


class UserAccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email address must be provided')

        if not password:
            raise ValueError('Password must be provided')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True

        return self._create_user(email, password, **extra_fields)


class User(PermissionsMixin, AbstractBaseUser):
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = UserAccountManager()

    email = models.EmailField('Email', unique=True, blank=False, null=False)
    full_name = models.CharField('Full name', blank=True, null=True, max_length=400)
    is_staff = models.BooleanField('Staff status', default=False)
    is_active = models.BooleanField('Active', default=True)
    is_verified = models.BooleanField('verified', default=False)  # Add the `is_verified` flag
    verification_uuid = models.UUIDField('Unique Verification UUID', default=uuid.uuid4)

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.email

    def __unicode__(self):
        return self.email


def user_post_save(sender, instance, signal, *args, **kwargs):
    if not instance.is_verified:
        # Send verification email
        print(settings.DATABASES)

        send_mail(
            'Verify your QuickPublisher account',
            '',
            'from panaev',
            [instance.email],
            fail_silently=False,
            html_message='<html><body>Follow this link to verify your account: '
                         '<a href="http://localhost:8000%s">Verify</a></body></html>' % reverse(
                'auth:verify', kwargs={'uuid': str(instance.verification_uuid)})
        )


signals.post_save.connect(user_post_save, sender=User)
