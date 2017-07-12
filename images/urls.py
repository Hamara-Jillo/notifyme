from django.conf.urls import url, include
from rest_framework import routers
from images.views import UniversityLogoViewSet


router = routers.DefaultRouter()
router.register(r'university_logos', UniversityLogoViewSet)

urlpatterns = [
    url(r'^api/v1/', include(router.urls) ),
    url(r'^api/docs/', include('rest_framework.urls')),

]