from __future__ import unicode_literals

from django.db import models


class Student(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, blank=False)
    student_id = models.CharField(max_length=20, primary_key=True)
    father_name = models.CharField(max_length=150)
    mother_name = models.CharField(max_length=150)

    def __unicode__(self):
        return self.student_id + " " + self.name

    class Meta:
        ordering = ('student_id',)


class Subject(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    subject_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=150)

    def __unicode__(self):
        return self.subject_id + " " + self.name

    class Meta:
        ordering = ('subject_id',)


class Result(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    grade_id = models.AutoField(primary_key=True)
    grade = models.DecimalField(max_digits=5, decimal_places=3, blank=False)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)

