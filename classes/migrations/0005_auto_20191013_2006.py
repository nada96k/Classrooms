# Generated by Django 2.1.5 on 2019-10-13 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_auto_20191012_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='exam_grade',
            field=models.CharField(choices=[('-', 'NoGrade'), ('A', 'A'), ('A-', 'A-'), ('B+', 'B+'), ('B', 'B'), ('B-', 'B-'), ('C+', 'C+'), ('C', 'C'), ('C-', 'C-'), ('D+', 'D+'), ('D', 'D'), ('F', 'F'), ('FA', 'FA')], default='-', max_length=2),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('UNDEFINED', 'Undefined'), ('FEMALE', 'Female'), ('MALE', 'Male')], default='UNDEFINED', max_length=10),
        ),
    ]
