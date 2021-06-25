
from django.shortcuts import render,redirect
from time import gmtime, strftime,localtime
 
def index(request):
    return redirect('/time_display')
   
def time_display(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p ", localtime()),
        "Hora": strftime("%H:%M %p", localtime()),
        "Fecha": strftime("%Y-%m-%d" ,gmtime())
    }
    return render(request,'index.html', context)



