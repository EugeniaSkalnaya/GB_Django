from django.urls import path
from .views import greet, about

urlpatterns = [
    path("", greet, name="greet"),
    path("about/", about, name="about"),
]
