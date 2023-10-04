
from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="index"),
    path("greet/<str:name>", views.greet, name="greet"),
]
