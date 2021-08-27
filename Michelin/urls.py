from django.urls import path
from . import views

app_name = "michelin"
urlpatterns = [
    path("", views.index, name = "index"),
    path("new_category/", views.new_category, name = "new_category"),
    path("new_category/create", views.create_category, name = "create_category"),
    path("<int:restaurant_id>/", views.detail, name = "detail"),
    path("<int:restaurant_id>/delete", views.delete_detail, name = "delete_detail"),
    path("<int:restaurant_id>/update", views.update_detail, name = "update_detail")
]