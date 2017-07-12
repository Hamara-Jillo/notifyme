from rest_framework import viewsets
from notifyme.serializers import UniversityLogoSerializer
from images.models import UniversityLogo


class UniversityLogoViewSet(viewsets.ModelViewSet):

    queryset = UniversityLogo.objects.all()
    serializer_class = UniversityLogoSerializer
