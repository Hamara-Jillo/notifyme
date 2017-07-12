from rest_framework import serializers
from institute.models import Institute
from school.models import School
from department.models import Department
from programme.models import Programme
from course.models import Course
from images.models import UniversityLogo
from drf_extra_fields.fields import Base64ImageField
from rest_framework.fields import ImageField


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'code', 'title',
                  'units','description', 'year',
                  'semester', 'programme', 'choice')


class ProgrammeSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Programme
        fields = ('id', 'name', 'title', 'duration', 'department', 'courses')



class DepartmentSerializer(serializers.ModelSerializer):
    programmes = ProgrammeSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ('id', 'name', 'school', 'programmes')



class SchoolSerializer(serializers.ModelSerializer):
    departments = DepartmentSerializer(many=True, read_only=True)

    class Meta:
        model = School
        fields = ('id', 'name', 'institute','departments')


class UniversityLogoSerializer(serializers.ModelSerializer):
    image = ImageField(max_length=None, allow_empty_file=False)
    class Meta:
        model = UniversityLogo
        fields = ('id', 'image', 'name')


class InstituteSerializer(serializers.ModelSerializer):
    schools = SchoolSerializer(many=True, read_only=True)
    logo = UniversityLogoSerializer()

    class Meta:
        model = Institute
        fields = ('id', 'name', 'logo', 'schools')


    def create(self, validated_data):

        logo_data = validated_data.pop('logo', None)

        if logo_data:
            logo = UniversityLogo.objects.get_or_create(**logo_data)[0]
            validated_data['logo'] = logo

        return Institute.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.logo = validated_data.get('logo', instance.logo)
        instance.schools = validated_data.get('schools', instance.schools)
        instance.save()
        return instance