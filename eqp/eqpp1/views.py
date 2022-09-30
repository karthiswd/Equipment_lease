from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import signup, ldetails, addlease, client
from django.urls import reverse
from datetime import date


def index(request):
    return render(request, 'index.html')


def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == 'admin':
            return render(request, 'admins.html')
        else:
            return HttpResponse('Invalid Password')
    return render(request, 'adminlogin.html')


def admins(request):
    return render(request, 'admins.html')


def Pendings(request):
    Signup = signup.objects.all()
    return render(request, 'pendings.html', {'data': Signup})


def edit(request, id):
    Signup = signup.objects.get(count=id)
    return render(request,'admins.html', {'date': Signup})


def destroy(request, id):
    data = signup.objects.get(id=id)
    data.delete()
    return redirect('/pendings')


def update(request, id):
    data = signup.objects.get(id=id)
    data.Status = True
    data.save()
    return redirect('/pendings')


def update(request, id):
    data = signup.objects.get(id=id)
    data.Status = True
    data.save()
    return redirect('/pendings')


def Signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        file = request.FILES['file']
        users = signup()
        users.Name = name
        users.Username = username
        users.Password = password
        users.Email = email
        users.File = file
        users.save()
        if signup():
            return redirect(reverse('login'))
        else:
            return HttpResponse('Signup Failed')
    return render(request, 'Signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            signup.objects.get(Username=username, Password=password, Status=True)
            return render(request, 'customer.html')
        except:
            return HttpResponse('Invaild User')
    return render(request, 'login.html')


def leasordetails(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email_id = request.POST.get('email_id')
        phone = request.POST.get('phone')
        users = ldetails()
        users.Fname = fname
        users.Lname = lname
        users.Email_ID = email_id
        users.Phone = phone
        users.save()
        if ldetails():
            return HttpResponse('Sumbitted, Thank you')
        else:
            return HttpResponse('Signup Failed')
    return render(request, 'leasordetails.html')


def Addlease(request):
    if request.method == 'POST':
        wcountry = request.POST.get('wcountry')
        dcountry = request.POST.get('dcountry')
        contract_yr = request.POST.get('contract_yr')
        phone = request.POST.get('phone')
        users = addlease()
        users.Wcountry = wcountry
        users.Dcountry = dcountry
        users.Contract_yr = contract_yr
        users.Phone = phone
        users.save()


def admindetails(request):
    lsdetails = ldetails.objects.filter(Status=False)
    return render(request, 'admin.html', {'values': lsdetails})


def leasseview(request):
    details = addlease.objects.filter(Status=False)
    return render(request, 'admin.html', {'values': details})


def customer(request):
    if request.method == 'POST':
        size = request.POST.get('size')
        price = request.POST.get('price')
        containername = request.POST.get('containername')
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        users = client()
        users.Sizecontain = size
        users.Ratecontain = price
        users.Containername = containername
        users.Fromdate = fromdate
        users.Todate = todate
        users.save()
        if client():
            return redirect('/index')
        else:
            return HttpResponse('Something went wrong')
    return render(request, 'customer.html')