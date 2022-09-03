from django.shortcuts import render

from .models import Complaint, Student
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

class ComplaintList(ListView):
    model = Complaint
    # num_complaints = model.objects.all().count()
    context_object_name = 'complaints'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_complaints'] = context['complaints'].all().count()
        return context

class ComplaintAdd(CreateView):
    model = Complaint
    fields = ['student', 'group', 'quick_text', 'description',]
    success_url = reverse_lazy('complaint_list')

class ComplaintDetail(DetailView):
    model = Complaint
    context_object_name = 'detail'