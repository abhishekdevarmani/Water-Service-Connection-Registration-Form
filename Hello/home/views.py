from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import index_view
from django.contrib import messages
# Create your views here.
def index(request):
    if request.method == "POST":
        zroLocation = request.POST.get('zroLocation')
        ApplyFor = request.POST.get('ApplyFor')
        connectionType = request.POST.get('connectionType')
        firstName = request.POST.get('firstName')
        middleName = request.POST.get('middleName')
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        Mobile = request.POST.get('Mobile')
        Addr = request.POST.get('Addr')
        Land = request.POST.get('Land')
        pinAdd = request.POST.get('pinAdd')
        locaAdd = request.POST.get('locaAdd')
        subLoc = request.POST.get('subLoc')
        assem = request.POST.get('assem')
        vilAdd = request.POST.get('vilAdd')
        Index =index_view(zroLocation=zroLocation , ApplyFor=ApplyFor,connectionType=connectionType,firstName=firstName,middleName=middleName,lastName=lastName, email=email,Mobile=Mobile,Addr=Addr, Land=Land, pinAdd=pinAdd,locaAdd=locaAdd,subLoc=subLoc,assem=assem,vilAdd=vilAdd, date=datetime.today())
        Index.save()
        messages.success(request, "Your Message Has Been Sent.")
    return render(request,'index.html')
   

def about(request):
    return HttpResponse("This is Aboutpage")

def services(request):
    return HttpResponse("This is Servicespage")

def contact(request):
    return HttpResponse("This is Contactpage")