from rest_framework import permissions, viewsets
from rest_framework.response import Response
from .models import Institute, School, Programme, Department, Course
from .permissions import IsAuthorOfInstitute
from .serializers import InstituteSerializer, SchoolSerializer, DepartmentSerializer, ProgrammeSerializer, CourseSerializer

class InstituteViewSet(viewsets.ModelViewSet):
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class ProgrammeViewSet(viewsets.ModelViewSet):
    queryset = Programme.objects.all()
    serializer_class = ProgrammeSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
