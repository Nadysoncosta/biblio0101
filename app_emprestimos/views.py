from django.shortcuts import render

# Create your views here.
def index():
    return render(index,"base.html")