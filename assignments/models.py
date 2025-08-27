from django.db import models
from users.models import Student
from courses.models import Course

class Progress(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} - {self.course} - {self.completed}"


class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    due_date = models.DateField()

    def __str__(self):
        return self.title