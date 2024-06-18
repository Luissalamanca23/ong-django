from django.shortcuts import render
from .models import Mascota

# Create your views here.

def administrador(request):
    mascotas=Mascota.objects.all()
    context={'mascota':mascotas}
    return render(request,'crud/administrador.html',context)

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