from django.shortcuts import render, redirect
from datetime import datetime
from .models import Box, BoxItem
from .forms import BoxForm, BoxItemForm



def edit_item(request, item_id):
    item = BoxItem.objects.get(pk=item_id)

    form = BoxItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('box-list')

    return render(request, 'mainApp/edit_item.html',
    {'item': item,
    'form': form})


def delete_item(request, item_id):
    item = BoxItem.objects.get(pk=item_id)
    item.delete()
    return redirect('box-list')
    

def add_item(request, box_id):
    box = Box.objects.get(pk=box_id)
    if request.method == "POST":
        form = BoxItemForm(request.POST or None)
        if form.is_valid():
            box_item = form.save(commit=False)
            box_item.box = box
            box_item.item_creation_date = datetime.now()
            box_item.save()
            return redirect('box-list')
    else:
        form = BoxItemForm
        return render(request, 'mainApp/add_item.html',
        {'form': form})


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


def search_boxes(request):
    if request.method == "POST":
        searched = request.POST['searched']
        boxes = Box.objects.filter(box_number__contains=searched)
        box_Item_list = BoxItem.objects.all().order_by('item_creation_date')
        
        return render(request,
        'mainApp/search_boxes.html',
        {'searched': searched,
        'boxes': boxes,
        'box_Item_list': box_Item_list})
    else:
        return render(request,
        'mainApp/search_boxes.html',
        {})


def create_box(request):
    submitted = False
    if request.method == "POST":
        form = BoxForm(request.POST)
        if form.is_valid():
            box = form.save(commit=False)
            box.box_creation_date = datetime.now()
            box.save()
            return redirect('box-list')
    else:
        form = BoxForm
        if 'submitted' in request.GET:
            submitted = True   

    return render(request, 'mainApp/create_box.html', {
        'form':form,
    })
  

def box_list(request):
    box_list = Box.objects.all().order_by('box_number')
    box_Item_list = BoxItem.objects.all().order_by('item_creation_date')
    return render(request, 'mainApp/box_list.html',
        {'box_list': box_list,
        'box_Item_list': box_Item_list})


def home(request):
    return render(request, 'mainApp/home.html')