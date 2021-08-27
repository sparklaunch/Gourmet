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