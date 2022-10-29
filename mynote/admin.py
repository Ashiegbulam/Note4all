from django.contrib import admin
from mynote.models import Course, Topic, Note

admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(Note)