from rest_framework import serializers
from models import *


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('student_id', 'name', 'father_name', 'mother_name')


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ('subject_id', 'name')


class ResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Result
        fields = ('grade_id', 'grade', 'student_id', 'subject_id')
