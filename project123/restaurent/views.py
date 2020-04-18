from django.shortcuts import render,redirect
from restaurent.form import restarentForm


def ShowIndex(request):
    return render(request,'res/index.html')


def regiStation(request):
    return render(request,'res/registration.html',{"rf":restarentForm()})


def backMain(request):
    return redirect('restro')


def saveDetails(request):
    rf = restarentForm(request.POST)
    if rf.is_valid():
        dt =rf.save(commit=False)
        dt.otp = 5475
        rf.save()
        return redirect('restro')

