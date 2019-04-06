from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def customer_details(request):
    return render(request, 'admin_panel/customer_details.html')

@login_required
def customer_agent(request):
    return render(request, 'admin_panel/customer_agent.html')