from django.shortcuts import render

from .models import Complaint, Student
from django.views.generic.list import ListView

class ComplaintList(ListView):
    model = Complaint
    num_complaints = model.objects.all().count()
    context_object_name = 'complaints'