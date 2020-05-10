from django.contrib import admin
from .models import *


class SubcriberAdmin(admin.ModelAdmin):
    list_filter = ['user_name', 'user_email']
    search_fields = ['user_name', 'user_email']
    list_display = [field.name for field in Subscriber._meta.fields]

    class Meta:
        model = Subscriber


admin.site.register(Subscriber, SubcriberAdmin)
