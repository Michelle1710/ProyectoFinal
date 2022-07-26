from urllib import request
from django.shortcuts import render,redirect
from AppCoder.models import Servicio,Estado_revision
from django.http import HttpResponse
from django.template import loader

from AppCoder.form import ServicioFormulario, Estado_revisioFormulario
from django.db.models import Q

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
def servicios(request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            servicios = Servicio.objects.filter(Q(placa__icontains=search)).values()

            return render(request,"Taller/servicio.html",{"placa":servicios, "search":True, "busqueda":search})

    servicio = Servicio.objects.all()

    return render(request,"Taller/servicio.html",{"placa":servicio})

def crear_cliente(request):
    
    # post
    if request.method == "POST":
        
        formulario = ServicioFormulario(request.POST)

        if formulario.is_valid():
            
            info = formulario.cleaned_data

            cliente = Servicio(nombre=info["nombre"],apellido=info["apellido"],marca_de_carro=info["Marca de carro"],modelo=info["modelo"],placa=info["placa"],email=info["email"], descripcionRev=info["Descripción de revisión"])

            cliente.save()

            return redirect("Cliente")

        return render(request,"ProyectoCoderApp/formulario_usuario.html",{"form":formulario})

    # get
    formulario = ServicioFormulario()
    return render(request,"ProyectoCoderApp/formulario_usuario.html",{"form":formulario})

def eliminar_usuario(request,placa):

    usuario = Servicio.objects.get(placa=placa)
    usuario.delete()

    return redirect("Cliente")

def editar_usuario(request,placa):

    usuario = Servicio.objects.get(placa=placa)

    if request.method == "POST":

        formulario = ServicioFormulario(request.POST)

        if formulario.is_valid():
            
            info_usuario = formulario.cleaned_data
            
            usuario.nombre = info_usuario["nombre"]
            usuario.apellido = info_usuario["apellido"]
            usuario.email = info_usuario["email"]
            usuario.save()

            return redirect("Cliente")

    # get
    formulario = ServicioFormulario(initial={"nombre":usuario.nombre, "apellido":usuario.apellido, "email": usuario.email, "Marca de carro": usuario.marca_de_carro, "placa":usuario.placa, "Descripción de revisión":usuario.descripcionRev})
    

    
    return render(request,"ProyectoCoderApp/formulario_usuario.html",{"form":formulario})

class ServicioList(ListView):

    model = Servicio
    template_name = "ProyectoCoderApp/servicio_list.html"

class ServicioDetail(DetailView):

    model = Servicio
    template_name = "ProyectoCoderApp/servicio_detail.html"

class ServicioCreate(CreateView):

    model = Servicio
    success_url = "/coderapp/servicio/list" # atenciooooooooon!!!! a la primer /
    fields = ["nombre", "apellido","Modelo de carro", "placa","email","Descripción de revisión"]

class ServicioUpdate(UpdateView):

    model = Servicio
    success_url = "/coderapp/estudiante/list" # atenciooooooooon!!!! a la primer /
    fields = ["nombre", "apellido","Modelo de carro", "placa","email","Descripción de revisión"]

class ServicioDelete(DeleteView):

    model = Servicio
    success_url = "/coderapp/servicio/list"

def revision(request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            revision = Estado_revision.objects.filter( Q(placa__icontains=search) ).values()

            return render(request,"ProyectoCoderApp/revision.html",{"cursos":revision, "search":True, "busqueda":search})

    revision = Estado_revision.objects.all()

    return render(request,"ProyectoCoderApp/revision.html",{"revision":revision, "search":False})

def crear_rev(request):

    # post
    if request.method == "POST":

        formulario = Estado_revisioFormulario(request.POST)

        if formulario.is_valid():

            info_rev = formulario.cleaned_data
        
            rev = Estado_revision(nombre=info_rev["placa"])
            rev.save() 
            
            return redirect("revision")

        else:

            return render(request,"ProyectoCoderApp/formulario_revision.html",{"form":formulario,"accion":"Crear revision"})
    

    else: 

        formularioVacio = Estado_revisioFormulario()

        return render(request,"ProyectoCoderApp/formulario_revision.html",{"form":formularioVacio,"accion":"Crear revision"})

def eliminar_revision(request, placa):

    
    revision = Estado_revision.objects.get(placa=placa)
    revision.delete()

    return redirect("placa")

def editar_revision(request, placa):

    
    revision = Estado_revision.objects.get(placa=placa)

    if request.method == "POST":

        formulario = Estado_revisioFormulario(request.POST)

        if formulario.is_valid():

            info_rev = formulario.cleaned_data
        
            revision.placa = info_rev["placa"]
            revision.entrada = info_rev["entrada"]
            revision.tiporeparacion = info_rev["descripción"]
            revision.save()
            
            return redirect("revision")

            
    formulario = Estado_revisioFormulario(initial={"placa":revision.placa,"entrada":revision.entrada,"descrpcion":revision.tiporeparacion})

    return render(request,"ProyectoCoderApp/formulario_revision.html",{"form":formulario,"accion":"Editar revision"})
