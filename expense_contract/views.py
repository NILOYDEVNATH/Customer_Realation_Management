from django.shortcuts import render

# Create your views here.

def expense(request):
    return render(request, 'admin_panel/expense.html')


def contract(request):
    return render(request, 'admin_panel/contract.html')
