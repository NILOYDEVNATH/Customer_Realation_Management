from django.shortcuts import render

# Create your views here.

def category(request):
    return render(request, 'admin_panel/category.html')


def subcategory(request):
    return render(request, 'admin_panel/sub_category.html')


def item(request):
    return render(request, 'admin_panel/item.html')


def status(request):
    return render(request, 'admin_panel/status.html')