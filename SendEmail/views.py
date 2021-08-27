from django.shortcuts import render
from .models import Email

# Create your views here.
def index(request):
    address = request.POST["address"]
    title = request.POST["title"]
    content = request.POST["content"]
    new_email = Email(address = address, title = title, content = content)
    new_email.save()
    return render(request, "./email_index.html", {
        "address": address,
        "title": title,
        "content": content
    })