from rest_framework import viewsets
from notifyme.serializers import InstituteSerializer
from .models import Institute


class InstituteViewSet(viewsets.ModelViewSet):
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer







