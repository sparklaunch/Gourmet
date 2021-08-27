from django.urls import path
from . import views

app_name = "michelin"
urlpatterns = [
    path("", views.index, name = "index"),
    path("new_category/", views.new_category, name = "new_category"),
    path("new_category/create", views.create_category, name = "create_category"),
    path("<int:category_id>/restaurants", views.show_restaurants, name = "show_restaurants")
]