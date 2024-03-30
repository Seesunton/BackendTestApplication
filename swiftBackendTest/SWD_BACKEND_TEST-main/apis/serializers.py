

from rest_framework import serializers
from .models import StudentSubjectsScore, Personnel, Subjects, Classes, Schools,SchoolStructure

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ['class_order']

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schools
        fields = ['title']

class PersonnelSerializer(serializers.ModelSerializer):
    school_class = ClassSerializer()
    
    class Meta:
        model = Personnel
        fields = ['first_name', 'last_name', 'school_class', 'personnel_type']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ['title']

class StudentSubjectsScoreSerializer(serializers.ModelSerializer):
    student = PersonnelSerializer()
    subjects = SubjectSerializer()

    class Meta:
        model = StudentSubjectsScore
        fields = ['student', 'subjects', 'score']

class SchoolStructureSerializer(serializers.ModelSerializer):
    sub = serializers.ListSerializer(child=serializers.DictField(), required=False)  # เปลี่ยนจาก `self` เป็น `serializers.DictField()`

    class Meta:
        model = SchoolStructure
        fields = ['title', 'sub']
