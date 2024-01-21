from django.contrib import admin

from .models import Choice, Question


# site settings
admin.site.site_header = "My admin"

# register models
admin.site.register(Choice)
admin.site.register(Question)
