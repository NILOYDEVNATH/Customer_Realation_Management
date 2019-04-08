from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def sale(request):
    return render(request, 'admin_panel/proposal.html')

def estimate(request):
    return render(request, 'admin_panel/estimate.html')
