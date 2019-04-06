from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect

from zeep import Client

def message_sent(request):
    url = 'https://api2.onnorokomsms.com/sendsms.asmx?WSDL'
    client = Client(url)
    username = '01860872083'
    password = 'a96f7d7984'
    recipientNumber = ['01798509278']
    numberList = ",".join(recipientNumber)
    smsText = 'Hello,,, How Are You ? I am From Canda,,, I Love You,, I See You In Facebook,, You Are Nice,, Pokla Dat,,, Love You ,,'
    smsType = 'TEXT'
    maskName = ''
    campaignName = ''
    client.service.OneToMany(username,password,smsText,numberList,smsType,maskName,campaignName)



# Create your views here.
def dashboard_login(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'admin_panel/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            #message_sent(request)
            return HttpResponseRedirect(reverse('home'))
        else:
             return HttpResponseRedirect(reverse('login'))

@login_required
def dashboard_logout(request):
    logout(request)
    context = {
        'message' : 'Logout success'
    }
    return HttpResponseRedirect(reverse('login'))
    
@login_required
def home(request):
    return render(request, 'admin_panel/home.html')

