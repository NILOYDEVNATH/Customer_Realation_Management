from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import CustomeragentForm,CustomerdetailsForm,BillingFrom
from django.urls import reverse
from .models import *


# Create your views here.

@login_required
def customer_details(request):
    if request.method=="POST":
        form=CustomerdetailsForm(request.POST,request.FILES)
        billing=BillingFrom(request.POST)
        groups=request.POST.getlist('groups[]')
        if form.is_valid():
            form.save()
            if billing.is_valid():
                new_data=billing.save()
                for groups_data in groups:
                    groups_model=groupModel()
                    groups_model.customer_details=new_data
                    groups_model.group_data=groups_data
                    groups_model.save()
                return HttpResponseRedirect(reverse('customer_details'))
    else:
        form=CustomerdetailsForm()
        billing=BillingFrom()
    return render(request, 'admin_panel/customer_details.html',{'form':form,'billing':billing})

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
    
    
