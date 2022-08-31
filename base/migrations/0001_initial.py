# Generated by Django 4.1 on 2022-08-31 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('hostel', models.CharField(max_length=100)),
                ('room', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(choices=[('wf', 'Wifi'), ('et', 'Electrical'), ('ts', 'Toilets'), ('cp', 'Carpentry'), ('cl', 'Cleaning'), ('os', 'Others')], max_length=2)),
                ('quick_text', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('reported_date', models.DateField(auto_now_add=True)),
                ('resolved_date', models.DateField(blank=True, null=True)),
                ('resolved', models.BooleanField(default=False)),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='base.student')),
            ],
            options={
                'ordering': ['-reported_date'],
            },
        ),
    ]