from django.shortcuts import render
from django.http import HttpResponse
from .models import Mascota, Sexo



def index(request):
    contexto = {'mensaje': 'Pagina de inicio'}
    return render(request, 'index.html', contexto)

def animales_gato(request):
    mascota = Mascota.objects.order_by('?').first()
    contexto = {'mascota': mascota}
    return render(request, 'animales_gato.html', contexto)

def animales_perro(request):
    contexto = {'mensaje': 'Pagina de perros'}
    return render(request, 'animales_perro.html')

def perro(request):
    contexto = {'mensaje': 'Pagina de perros'}
    return render(request, 'perros.html')

def gato(request):
    return render(request, 'gatos.html')

def login(request):
    contexto = {'mensaje': 'Pagina de login'}
    return render(request, 'login.html')




def agregarMascota(request):
    if request.method is not "POST":
        sexos=Sexo.objects.all();
        context={'sexo':sexos}
        return render(request,'crud/agregar.html',context)
    else:
        #Es un POST,por lo tanto se recuperan los datos del formulario
        idMascota=request.POST["idMascota"]
        nombre=request.POST["nombreMascota"]
        fecha_nac=request.POST["fechaNac"]
        raza=request.POST["razaMascota"]
        sexo=request.POST["sexo"]
        activo="1"
    
        objSexo=Sexo.objects.get(id_sexo = sexo)
        obj=Mascota.objects.create(id_mascota=idMascota,
                                   nombre_mascota=nombre,
                                   fecha_nacimiento=fecha_nac,
                                   raza_mascota=raza,
                                   id_sexo=objSexo,
                                   activo=1)
        obj.save()
        context={'mensaje':'OK, datos guardados con éxito'}
        return render(request,'crud/agregar.html',context)


def encontrarMascota(request,pk):
    if pk != " ":
        mascota=Mascota.objects.get(id_mascota=pk)
        sexos=Sexo.objects.all()
        print(type(mascota.id_sexo.sexo))
    context={'mascota':mascota,'sexo':sexos}
    if mascota:
        return render(request,'crud/modificar.html',context)
    else:
        context={'mensaje':'Error, id mascota no existe'}
        return render(request,'crud/admin.html',context)
    

def modificarMascota(request):

    if request.method=="POST":
        idMascota=request.POST["idMascota"]
        nombre=request.POST["nombreMascota"]
        fecha_nac=request.POST["fechaNac"]
        raza=request.POST["razaMascota"]
        sexo=request.POST["sexo"]
        activo="1"
    
        objSexo=Sexo.objects.get(id_sexo = sexo)

        mascota=Mascota()
        mascota.id_mascota=idMascota
        mascota.nombre_mascota=nombre
        mascota.fecha_nacimiento=fecha_nac
        mascota.raza_mascota=raza
        mascota.id_sexo=objSexo
        mascota.activo=1
        mascota.save()
        sexos=Sexo.objects.all()
        context={'mensaje':'OK, datos actualizados con éxito','sexo':sexos,'mascota':mascota}
        return render(request,'crud/modificar.html',context)
    else:
        mascota=Mascota.objects.all()
        context={'mascota':mascota}
        return render(request,'crud/admin.html',context)


def eliminarMascota(request,pk):
    context={}
    try:
        mascota=Mascota.objects.get(id_mascota=pk)
        mascota.delete()
        mensaje="Ok, Datos eliminados satisfactoriamente"
        mascotas=Mascota.objects.all()
        context={'mascota':mascotas,'mensaje':mensaje}
        return render(request,'crud/admin.html',context)
    except:
        mensaje="Error, id mascota no existe"
        mascotas=Mascota.objects.all()
        context={'mascota':mascotas,'mensaje':mensaje}
        return render(request,'crud/admin.html',context)

