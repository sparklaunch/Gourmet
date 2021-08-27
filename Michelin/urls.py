from django.urls import path
from . import views

app_name = "michelin"
urlpatterns = [
    path("", views.index, name = "index")
]