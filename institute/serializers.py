from rest_framework import serializers
from .models import Institute, School,Department, Programme, Course

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'code', 'title',
                  'units','description', 'year',
                  'semester', 'programme', 'choice')
        read_only_fields = 'id'

class ProgrammeSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Programme
        fields = ('id', 'name', 'title', 'duration', 'department', 'courses')
        read_only_fields = 'id'


class DepartmentSerializer(serializers.ModelSerializer):
    programmes = ProgrammeSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ('id', 'name', 'school', 'programmes')
        read_only_fields = 'id'


class SchoolSerializer(serializers.ModelSerializer):
    departments = DepartmentSerializer(many=True, read_only=True)

    class Meta:
        model = School
        fields = ('id', 'name', 'institute','departments')
        read_only_fields = 'id'


class InstituteSerializer(serializers.ModelSerializer):
    schools = SchoolSerializer(many=True, read_only=True)
    logo = serializers.ImageField(use_url=False)

    class Meta:
        model = Institute
        fields = ('id', 'name', 'logo', 'schools')
        read_only_fields = 'id'


