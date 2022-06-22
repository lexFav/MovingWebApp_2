from django.shortcuts import render, redirect
from datetime import datetime
from .models import Box, BoxItem
from .forms import BoxForm, BoxItemForm
from django.http import HttpResponseRedirect


def delete_box(request, box_id):
    box = Box.objects.get(pk=box_id)
    box.delete()
    return redirect('box-list')

def edit_box(request, box_id):
    box = Box.objects.get(pk=box_id)

    form = BoxForm(request.POST or None, instance=box)

    if form.is_valid():
        form.save()
        return redirect('box-list')

    return render(request, 'mainApp/edit_box.html',
    {'box': box,
    'form': form})


def create_box(request):
    submitted = False
    if request.method == "POST":
        form = BoxForm(request.POST)
        if form.is_valid():
            box = form.save(commit=False)
            box.box_creation_date = datetime.now()
            box.save()
            return HttpResponseRedirect('/create_box?submitted=True')
    else:
        form = BoxForm
        if 'submitted' in request.GET:
            submitted = True   

    return render(request, 'mainApp/create_box.html', {
        'form':form,
    })
  

def box_list(request):
    box_list = Box.objects.all().order_by('box_number')
    return render(request, 'mainApp/box_list.html',
        {'box_list': box_list})


def home(request):
    return render(request, 'mainApp/home.html')