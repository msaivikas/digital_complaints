from django.db import models


class Complaint(models.Model):
    student = models.ForeignKey('Student', on_delete=models.RESTRICT, null=True, blank=True) # one complaint<->one student but one student<->many complaints; On deleting a complaint, student shouldn't be deleted.
    GROUP =(
        ('wf', 'Wifi'),
        ('et', 'Electrical'),
        ('ts', 'Toilets'),
        ('cp', 'Carpentry'),
        ('cl', 'Cleaning'),
        ('os', 'Others'),
    )
    group = models.CharField(max_length=2, choices=GROUP,)
    quick_text = models.CharField(max_length=100,)
    description = models.TextField(max_length=500, blank=True, null=True)
    reported_date = models.DateField(auto_now_add=True)
    resolved_date = models.DateField(null=True, blank=True)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return self.quick_text

    class Meta:
        ordering = ['-reported_date']

class Student(models.Model):
    student_name = models.CharField(max_length=100,)
    hostel = models.CharField(max_length=100)
    room = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.student_name
