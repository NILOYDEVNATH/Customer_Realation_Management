from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import CustomeragentForm
from django.urls import reverse
from .models import *


# Create your views here.

@login_required
def customer_details(request):
    return render(request, 'admin_panel/customer_details.html')

@login_required
def customer_agent(request):
    if request.method=='POST':
        form=CustomeragentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('customer_agent'))
    else:
        form=CustomeragentForm()
    return render(request, 'admin_panel/customer_agent.html',{'form':form})


def customeragent_view(request):
    value=CustomeragetModel.objects.all()
    return render(request,'admin_panel/customeragent_view.html',{'value':value})

def customeragent_delete(request,pk):
    value=CustomeragetModel.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('customeragent_view'))

def customeragent_edit(request,pk):
    value=CustomeragetModel.objects.all()
    data=CustomeragetModel.objects.get(pk=pk)
    if request.method=='POST':
        form=CustomeragentForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('customeragent_view'))
    else:
        form=CustomeragentForm(instance=data)
    return render(request,'admin_panel/customeragent_edit.html',{'form':form})
    
    
