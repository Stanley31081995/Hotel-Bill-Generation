from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def hotel_bill(request):
    return render(request,'home.html')

def bill(request):
    vada=7
    idly=8
    dosa=10
    val1=int(request.POST['no_of_vada'])
    val2=int(request.POST['no_of_idli'])
    val3=int(request.POST['no_of_dosa'])
    res= (val1*vada) + (val2*idly) + (val3*dosa)
    time=datetime.datetime.now()
    overall={'display_date':time,'Res':res}
    return render(request,"result.html", context=overall)


   