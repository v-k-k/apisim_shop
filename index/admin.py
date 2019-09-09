from django.contrib import admin
from .models import *

class SubscrberAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Subscriber._meta.fields]#[:-1]]
    list_filter = ("name",)
    search_fields = ["email", "mobile"]
    #fields = []
    #exclude = ["email"]


    class Meta:
        model = Subscriber

admin.site.register(Subscriber, SubscrberAdmin)
