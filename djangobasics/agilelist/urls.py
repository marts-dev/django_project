from django.urls import path

from agilelist import views

app_name = "agilelist"
urlpatterns = [
    path("statements/", views.StatementList.as_view(), name="list"),
    path("statements/<int:pk>/", views.StatementDetail.as_view(), name="detail"),
    path("statements/values/", views.ValueList.as_view(), name="values"),
    path("statements/principles/", views.PrincipleList.as_view(), name="principles"),
]
