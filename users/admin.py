from django.contrib import admin
from .models import Course, Enrollment, Student, StudentProfile

# Register your models here.
admin.site.register(Course)
admin.site.register(Enrollment)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "progress")
    search_fields = ("user__username",)

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user")
    search_fields = ("user__username",)