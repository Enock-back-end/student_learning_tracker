from django.contrib import admin
from .models import Assignment, Progress

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "course", "student", "due_date")
    search_fields = ("title", "course__title", "student__user__username")

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "course", "completed")
    list_filter = ("completed",)
