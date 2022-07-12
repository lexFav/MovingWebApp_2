from django.shortcuts import render, redirect
from datetime import datetime
from .models import Box, BoxItem
from .forms import BoxForm, BoxItemForm
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView

def search_box_item(request):
    if request.method == "POST":
        searched = request.POST['searched']
        box_items = BoxItem.objects.filter(item_name__icontains = searched)
        
        return render(request,
        'mainApp/search_box_item.html',
        {'searched': searched,
        'box_items': box_items,})
    else:
        return render(request,
        'mainApp/search_box_item.html',
        {})


def print_pdf(request):
    if request.method == "POST":
        searched = request.POST['searched_2'].split(",")
        searched_blank = request.POST['searched_2']

        if searched_blank:
            searched = request.POST['searched_2'].split(",")
            box_list = Box.objects.filter(box_number__in= searched)
        else:
            box_list = Box.objects.all().order_by('box_number')

    box_Item_list = BoxItem.objects.all().order_by('item_creation_date')
    template_path = 'mainApp/print_pdf.html'
    context = {'box_list': box_list,'box_Item_list': box_Item_list}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if downloade
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    #else
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



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
        searched = request.POST['searched'].split(",")
        searched_blank = request.POST['searched']

        if searched_blank:
            boxes = Box.objects.filter(box_number__in=searched)
        else:
            boxes = Box.objects.all().order_by('box_number')
            
        box_Item_list = BoxItem.objects.all().order_by('item_creation_date')
        
        return render(request,
        'mainApp/search_boxes.html',
        {'searched': searched,
        'boxes': boxes,
        'box_Item_list': box_Item_list})
    else:
        return render(request,
        'mainApp/search_boxes.html',{})


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