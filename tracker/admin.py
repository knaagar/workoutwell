from django.contrib import admin
from .models import personal_details, goals, exercise_tracker, blog

# Register your models here.
admin.site.register(personal_details)
admin.site.register(goals)
admin.site.register(exercise_tracker)
admin.site.register(blog)