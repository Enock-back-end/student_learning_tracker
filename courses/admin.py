from django.contrib import admin
from .models import Course, Enrollment

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at")
    search_fields = ("title",)

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "course", "progress", "enrolled_at")
    list_filter = ("course",)
    search_fields = ("user__username", "course__title")
