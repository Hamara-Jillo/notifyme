from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework_nested import routers
from authentication.views import AccountViewSet, LoginView, LogoutView
from notifyme.views import IndexView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from institute.views import InstituteViewSet
from school.views import SchoolViewSet
from department.views import DepartmentViewSet
from programme.views import ProgrammeViewSet
from course.views import CourseViewSet


router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'institutes', InstituteViewSet, base_name='institutes')
institute_router = routers.NestedSimpleRouter(router, r'institutes', lookup='institute')
institute_router.register(r'schools', SchoolViewSet, base_name='schools')
school_router = routers.NestedSimpleRouter(institute_router, r'schools', lookup='school')
school_router.register(r'departments', DepartmentViewSet, base_name='departments')
department_router = routers.NestedSimpleRouter(school_router, r'departments', lookup='department')
department_router.register(r'programmes', ProgrammeViewSet, base_name='programmes')
programme_router = routers.NestedSimpleRouter(department_router, r'programmes', lookup='programme')
programme_router.register(r'courses', CourseViewSet, base_name='courses')
course_router = routers.NestedSimpleRouter(programme_router, r'courses', lookup='course')
urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin$', include(admin.site.urls)),
    url(r'^api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/docs/', include('rest_framework_swagger.urls')),
    url(r'^api/v1/', include(router.urls,  namespace='api_v1')),
    url(r'^api/v1/', include(institute_router.urls)),
    url(r'^api/v1/', include(school_router.urls)),
    url(r'^api/v1/', include(department_router.urls)),
    url(r'^api/v1/', include(programme_router.urls)),
    url(r'^api/v1/', include(course_router.urls)),
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),
    url('^.*$', IndexView.as_view(), name='index'),
)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)