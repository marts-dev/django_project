from django.contrib import admin
from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Agile API",
      default_version='v1',
      description="REST API for retrieving Agile values and principles",
   ),
   public=False,
   permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
)

urlpatterns = [
    path("", include("agilelist.urls")),
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]
