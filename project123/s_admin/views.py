from django.shortcuts import render,redirect

from s_admin.models import *
from django.contrib import messages
from s_admin.forms import *
from restaurent.models import RegistrationFrom


def showIndex(request):
    return render(request,'s_admin/login_page.html')


def adminCheck(request):
    user = request.POST.get('a_username')
    pas = request.POST.get('a_password')
    try:
        LoginModel.objects.get(username=user,password=pas)
        request.session['status'] = True
        return redirect('admin_menu')
    except:
        messages.error(request,'invalide details')
        return redirect('main')


def adminMenu(request):
    return render(request, 's_admin/adminmenu.html')


def adminLogout(request):
    request.session['status'] = False
    return redirect('admin_menu')


def stateOperations(request):

    da = StateModel.objects.all()

    return render(request, 's_admin/state_operations.html', {"sf":stateForm(),"da":da})


def adminOperatoin(request):
    return redirect('admin_menu',)


def saveState(request):
    sf = stateForm(request.POST)
    if sf.is_valid():
        sf.save()
        return redirect('state_operations')


def updatestate(request):
    dt = StateModel.objects.all()
    no = request.GET.get('pno')
    data = StateModel.objects.get(sno=no)
    return render(request,'s_admin/state_operations.html',{"da":dt,"data":data})


def updatestated(request):
    no = request.GET.get('pno')
    st = request.POST.get('state')
    StateModel.objects.filter(sno=no).update(sname=st)
    return redirect('state_operations')


def deletestate(request):
    no = request.GET.get('pno')
    StateModel.objects.get(sno=no).delete()
    return redirect('state_operations')


def addCity(request):

    return render(request,'s_admin/addcity.html',{"cf":CityForm(),"data":CityModel.objects.all()})


def savecity(request):
    cf = CityForm(request.POST)
    if cf.is_valid():
        cf.save()
        return redirect('addcity')


def deletCity(request):
    no = request.GET.get('pno')
    CityModel.objects.filter(cno=no).delete()
    return redirect('addcity')


def updateCity(request):
    no = request.GET.get('pno')

    return render(request,'s_admin/addcity.html',{"dt": CityModel.objects.get(cno=no),"data":CityModel.objects.all()})


def updateSave(request):
    no = request.GET.get('pno')
    cn = request.POST.get('cityname')
    sn = request.POST.get('statename')
    CityModel.objects.filter(cno=no).update(cno=no,cname=cn)
    return redirect('addcity')


def areaOperations(request):

    return render(request,'s_admin/areaoperations.html',{"af":AreaForm(),"data":AreaOperations.objects.all()})


def saveArea(request):
    af = AreaForm(request.POST)
    if af.is_valid():
        af.save()
        return redirect('areaoperations')
    else:
        return render(request,'s_admin/areaoperations.html',{"af":AreaForm()})


def deleteArea(request):
    no = request.GET.get('pno')
    AreaOperations.objects.filter(ano=no).delete()
    return redirect('areaoperations')


def restroType(request):

    return render(request, 's_admin/restrotype.html', {"rf":RestroFrom(), "data":Restrotype.objects.all()})


def typeSave(request):
    tf = RestroFrom(request.POST)
    if tf.is_valid():
        tf.save()
    return redirect('restrotype')

def pending_res(request):
    rs = RegistrationFrom.objects.filter(restro_status='pending')
    return render(request,"s_admin/pending_res.html",{"data":rs})


def approve_res(request):
    rno = request.GET.get("rno")
    RegistrationFrom.objects.filter(restro_id=rno).update(restro_status='approved')
    return redirect('admin_home')


def cancel_res(request):
    rno = request.GET.get("rno")
    RegistrationFrom.objects.filter(restro_id=rno).update(restro_status='cancel')
    return redirect('admin_home')


def show_approved_res(request):
    rs = RegistrationFrom.objects.filter(restro_status='approved')
    return render(request, "s_admin/approved_res.html", {"data": rs})


def show_cancel_res(request):
    rs = RegistrationFrom.objects.filter(restro_status='cancel')
    return render(request, "s_admin/cancel_res.html", {"data": rs})

