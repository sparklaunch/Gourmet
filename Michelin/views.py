from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Category, Restaurant

# Create your views here.
def index(request):
    categories = Category.objects.all()
    restaurants = Restaurant.objects.all()
    return render(request, "./index.html", {
        "categories": categories,
        "restaurants": restaurants
    })

def new_category(request):
    return render(request, "./new_category.html", {})

def create_category(request):
    name = request.POST["name"]
    category = Category(name = name)
    category.save()
    return HttpResponseRedirect(reverse("michelin:index"))

def show_restaurants(request, category_id):
    selected_category = Category.objects.get(id = category_id)
    restaurants = selected_category.restaurant_set.all()
    return render(request, "./restaurants.html", {
        "category": selected_category,
        "restaurants": restaurants
    })

def new_restaurant(request, category_id):
    selected_category = Category.objects.get(id = category_id)
    return render(request, "./new_restaurant.html", {
        "category": selected_category
    })

def create_restaurant(request, category_id):
    selected_category = Category.objects.get(id = category_id)
    name = request.POST["name"]
    link = request.POST["link"]
    description = request.POST["description"]
    keyword = request.POST["keyword"]
    new_restaurant = Restaurant(name = name, link = link, description = description, keyword = keyword, category = selected_category)
    new_restaurant.save()
    return HttpResponseRedirect(reverse("michelin:show_restaurants", args = (category_id,)))

def show_detail(request, category_id, restaurant_id):
    selected_category = Category.objects.get(id = category_id)
    selected_restaurant = selected_category.restaurant_set.get(id = restaurant_id)
    return render(request, "./restaurant_detail.html", {
        "category": selected_category,
        "restaurant": selected_restaurant
    })

def delete_category(request, category_id):
    Category.objects.filter(id = category_id).delete()
    return HttpResponseRedirect(reverse("michelin:index"))