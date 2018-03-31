from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from django import forms

from authentication.forms import EmailUserCreationForm, EmailUserChangeForm


@admin.register(get_user_model())
class UserAdmin(UserAdmin):
    form = EmailUserChangeForm
    list_display = ('email', 'full_name', 'is_staff')
    ordering = ('email',)
    add_form = EmailUserCreationForm
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal info'), {'fields': ('full_name',)}),
        (('Permissions'), {'fields': ('is_active', 'is_verified', 'is_staff', 'is_superuser',
                                      'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login',)}),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    search_fields = ('email', 'full_name')
