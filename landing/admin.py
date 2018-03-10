from django.contrib import admin

# Register your models here.
from landing.models import Subscriber

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    class Meta():
        model = Subscriber

    list_display = [field.name for field in Subscriber._meta.fields]
    list_filter = ['name']
    search_fields = ['name', 'email']

