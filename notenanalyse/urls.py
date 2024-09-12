from django.urls import path
from . import views

app_name = "notenanalyse"

urlpatterns = [
    path("", views.index, name="index"),
]
