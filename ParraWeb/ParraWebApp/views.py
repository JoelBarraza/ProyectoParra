from django.shortcuts import render, HttpResponse, redirect
from ParraWebApp.models import tarea_n 
from .forms import tareaform
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = "/login")

def inicio(request):    
    context = {
        "list_tareas": tarea_n.objects.filter(estado = 0),  
        "list_terminadas" : tarea_n.objects.filter(estado = 1)     
    }
    return render(request,"ParraWebApp/Inicio.html",context)

def login(request):
    return render(request, "ParraWebApp/login.html")

def menu(request):  
    return render(request,"ParraWebApp/Menu.html")
    
def insert(request):
    if request.method == 'POST':
        print(request.POST)
        form = tareaform(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('inicio/')
    else:
        form = tareaform()  
    return render(request,"ParraWebApp/insertar.html", {'form':tareaform})  
    
def editartarea(request,id):
    tarea = tarea_n.objects.get(id = id)
    if request.method == "GET":
        form = tareaform(instance=tarea)
    else:
        form = tareaform(request.POST,instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('/inicio')
    return render (request,"ParraWebApp/insertar.html",{'form':form})
  
def terminartarea(request,id):
    tarea = tarea_n.objects.get(id = id)
    tarea.estado = 1
    tarea.save()
    return redirect('/inicio')

def eliminartarea(request, id):
    tarea = tarea_n.objects.get(id=id)
    tarea.delete()
    return redirect('/inicio')


    