from django.contrib import admin
from todoapp.models import Entry, Topic

# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)