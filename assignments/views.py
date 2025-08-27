from django.shortcuts import render
from .models import Assignment

def assignment_list(request, course_id):
    assignments = Assignment.objects.filter(course_id=course_id)
    return render(request, 'assignments/list.html', {'assignments': assignments})
