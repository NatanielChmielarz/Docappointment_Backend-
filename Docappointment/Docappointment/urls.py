

from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
schema_view = get_schema_view(
    openapi.Info(
        title="Episyche Technologies",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('account/',include('user_app.api.urls')),
    path('specialization/',include('specialization.api.urls')),
    path('medical_faciliti/',include('medical_facility.api.urls')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)