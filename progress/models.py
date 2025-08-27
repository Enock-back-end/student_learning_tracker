from django.db import models
from django.contrib.auth.models import User
from assignments.models import Assignment

class Progress(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.username} - {self.assignment.title} - {self.is_completed}"
