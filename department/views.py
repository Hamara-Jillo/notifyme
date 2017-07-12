from rest_framework import viewsets
from .models import Department
from notifyme.serializers import DepartmentSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

