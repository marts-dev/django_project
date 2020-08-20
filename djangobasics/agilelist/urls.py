from django.urls import path, include
from rest_framework.routers import DefaultRouter
from agilelist import views

router = DefaultRouter()
router.register("", views.StatementViewSet)
router.register("values", views.ValueList, basename="values")
router.register("principles", views.PrincipleList, basename="principles")

app_name = "agilelist"

urlpatterns = [path("statements/", include(router.urls))]
