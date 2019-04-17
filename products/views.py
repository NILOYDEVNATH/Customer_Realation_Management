from django.shortcuts import render
from .forms import categoryform,SubCategoryForm,ItemForm,StatusForm
from .models import *
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.core import serializers

# Create your views here.

def category(request):
    value = CategoryModel.objects.all()
    if request.method == 'POST':
        form = categoryform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Category Added Successfully')
            return HttpResponseRedirect(reverse('category'))
    else:
        form = categoryform()
    return render(request, 'admin_panel/category.html',{'form':form,'value':value})

def category_status_changed(request,pk):
    value = CategoryModel.objects.get(pk=pk)
    if value.category_status=='Active':
        value.category_status='Inactive'
        messages.success(request,'Status updated Successfully')
    else:
        value.category_status='Active'
        messages.success(request,'Status updated Successfully')
    value.save()
    return HttpResponseRedirect(reverse('category'))

def category_delete(request,pk):
    value = CategoryModel.objects.get(pk=pk).delete()
    messages.success(request,'Category Deleted Successfully')
    return HttpResponseRedirect(reverse('category'))

def category_edit(request,pk):
    value = CategoryModel.objects.all()
    data =  CategoryModel.objects.get(pk=pk)
    if request.method == 'POST':
        form = categoryform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            messages.success(request,'Category Updated Successfully')
            return HttpResponseRedirect(reverse('category'))
    else:
        form = categoryform(instance=data)
    return render(request, 'admin_panel/category_edit.html',{'form':form})


def subcategory(request):
    value=SubcategoryModel.objects.all()
    if request.method=="POST":
        form = SubCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('subcategory'))
    else:
        form = SubCategoryForm()
    context={
        'form':form,
        'value':value
    }    
    return render(request, 'admin_panel/sub_category.html',context)

def subcategory_delete(request,pk):
    value=SubcategoryModel.objects.filter(pk=pk).delete()
    return HttpResponseRedirect(reverse('subcategory'))

def subcategory_status_changed(request,pk):
    value=SubcategoryModel.objects.get(pk=pk)
    if value.sub_category_status=='Active':
        value.sub_category_status='Inactive'
    else:
        value.sub_category_status='Active'
    value.save()
    return HttpResponseRedirect(reverse('subcategory'))

def subcategory_edit(request,pk):
    value=SubcategoryModel.objects.all()
    data=SubcategoryModel.objects.get(pk=pk)
    if request.method=='POST':
        form=SubCategoryForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('subcategory'))
    else:
        form=SubCategoryForm(instance=data)
    return render(request, 'admin_panel/subcategory_edit.html',{'form':form})

def get_sub_category(request):
    category=request.POST.get('category')
    data=SubcategoryModel.objects.filter(category_name=category)
    value = serializers.serialize('json', data)
    return HttpResponse(value, content_type="application/json")

def item(request):
    value=ItemModel.objects.all()
    if request.method == 'POST':
        form=ItemForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('item'))
    else:
        form=ItemForm()
    return render(request, 'admin_panel/item.html',{'form':form,'value':value})

def item_delete(request,pk):
    value=ItemModel.objects.filter(pk=pk).delete()
    return HttpResponseRedirect(reverse('item'))

def item_update(request,pk):
    value=ItemModel.objects.all()
    data=ItemModel.objects.get(pk=pk)
    if request.method=='POST':
        form = ItemForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('item'))
    else:
        form = ItemForm(instance=data)
    return render(request, 'admin_panel/item_update.html',{'form':form})



def status(request):
    if request.method=='POST':
        form=StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('status'))
    else:
        form=StatusForm()
    return render(request, 'admin_panel/status.html',{'form':form})