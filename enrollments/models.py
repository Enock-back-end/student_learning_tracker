from django.db import models
from django.contrib.auth.models import User
from courses.models import Course

class Enrollment(models.Model):
  
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollment_students')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollment_courses')
    date_enrolled = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.course.title}"