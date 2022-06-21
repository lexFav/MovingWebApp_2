from django.shortcuts import render, redirect

def create_box(request):
    return render(request, 'mainApp/create_box.html')
  

def box_list(request):
    return render(request, 'mainApp/box_list.html')


def home(request):
    return render(request, 'mainApp/home.html')