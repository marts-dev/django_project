from django.urls import re_path, include
from rest_framework.routers import DefaultRouter
from agilelist import views
from django_filters.views import FilterView
from agilelist.filters import StatementFilter

router = DefaultRouter()
router.register(r"statements", views.StatementViewSet, basename="statements")
router.register(r"values", views.ValueViewSet, basename="values")
router.register(r"principles", views.PrincipleViewSet, basename="principles")

app_name = "agilelist"

urlpatterns = [
    re_path(r"", include(router.urls)),
    re_path(
        r"^filter/",
        FilterView.as_view(
            filterset_class=StatementFilter, template_name="filter/search.html"
        ),
    ),
]
