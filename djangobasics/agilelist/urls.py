from django.urls import path, include
from rest_framework.routers import DefaultRouter
from agilelist import views
from django_filters.views import FilterView
from agilelist.filters import StatementFilter

router = DefaultRouter()
router.register("", views.StatementViewSet)
router.register("values", views.ValueList, basename="values")
router.register("principles", views.PrincipleList, basename="principles")

app_name = "agilelist"

urlpatterns = [
    path("statements/", include(router.urls)),
    path(
        "filter/",
        FilterView.as_view(
            filterset_class=StatementFilter, template_name="filter/search.html"
        ),
    ),
]
