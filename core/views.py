from django.shortcuts import render, redirect

# Create your views here.
def core_home(request):
    return redirect('https://www.google.com')