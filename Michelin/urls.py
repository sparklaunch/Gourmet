from django.urls import path
from . import views

app_name = "michelin"
urlpatterns = [
    path("", views.index, name = "index"),
    path("new_category/", views.new_category, name = "new_category"),
    path("new_category/create", views.create_category, name = "create_category"),
    path("<int:category_id>/delete", views.delete_category, name = "delete_category"),
    path("<int:category_id>/restaurants", views.show_restaurants, name = "show_restaurants"),
    path("<int:category_id>/restaurants/new_restaurant", views.new_restaurant, name = "new_restaurant"),
    path("<int:category_id>/restaurants/new_restaurant/create", views.create_restaurant, name = "create_restaurant"),
    path("<int:category_id>/restaurants/<int:restaurant_id>", views.show_detail, name = "show_detail")
]