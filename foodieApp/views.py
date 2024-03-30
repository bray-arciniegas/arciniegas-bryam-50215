from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import *
from .forms import *

def home (request):
    return render(request, "foodieApp/home.html")

def recetario(request):
    recetas = Receta.objects.all()
    return render(request, "foodieApp/recetario.html", {"recetas": recetas})

def detalle_receta(request, receta_id):
    receta = get_object_or_404(Receta, pk=receta_id)
    return render(request, "foodieApp/detalle_receta.html", {"receta": receta})

def agregar_receta(request):
    if request.method == "POST":
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.autor = request.user
            form.save()
            return redirect("recetario")
    else:
        form = RecetaForm()
    return render(request, "foodieApp/agregar_receta.html", {"form": form})

def editar_receta(request, receta_id):
    receta = get_object_or_404(Receta, pk=receta_id)
    if request.method == "POST":
        form = RecetaForm(request.POST, request.FILES, instance=receta)
        if form.is_valid():
            form.save()
            return redirect("recetario")
    else:
        form = RecetaForm(instance=receta)
    return render(request, "foodieApp/editar_receta.html", {"form": form})

def eliminar_receta(request, receta_id):
    receta = get_object_or_404(Receta, pk=receta_id)
    if request.method == "POST":
        receta.delete()
        return redirect("recetario") 
    return render(request, "foodieApp/borrar_receta.html", {"receta": receta})

def coctelero(request):
    cocteles = Coctel.objects.all()
    return render(request, "foodieApp/coctelero.html", {"cocteles": cocteles})

def detalle_coctel(request, coctel_id):
    coctel = get_object_or_404(Coctel, pk=coctel_id)
    return render(request, "foodieApp/detalle_coctel.html", {"coctel": coctel})

def agregar_coctel(request):
    if request.method == "POST":
        form = CoctelForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.autor = request.user
            form.save()
            return redirect("coctelero")
    else:
        form = CoctelForm()
    return render(request, "foodieApp/agregar_coctel.html", {"form": form})

def editar_coctel(request, coctel_id):
    coctel = get_object_or_404(Coctel, pk=coctel_id)
    if request.method == "POST":
        form = CoctelForm(request.POST, request.FILES, instance=coctel)
        if form.is_valid():
            form.save()
            return redirect("coctelero")
    else:
        form = CoctelForm(instance=coctel)
    return render(request, "foodieApp/editar_coctel.html", {"form": form})

def eliminar_coctel(request, coctel_id):
    coctel = get_object_or_404(Coctel, pk=coctel_id)
    if request.method == "POST":
        coctel.delete()
        return redirect("coctelero") 
    return render(request, "foodieApp/borrar_coctel.html", {"coctel": coctel})

def lista_tips(request):
    tips = Tip.objects.all()
    return render(request, "foodieApp/lista_tips.html", {"tips": tips})

def agregar_tip(request):
    if request.method == "POST":
        form = TipForm(request.POST)
        if form.is_valid():
            form.instance.autor = request.user
            form.save()
            return redirect("lista_tips")
    else:
        form = TipForm()
    return render(request, "foodieApp/agregar_tip.html", {"form": form})

def editar_tip(request, tip_id):
    tip = get_object_or_404(Tip, pk=tip_id)
    if request.method == "POST":
        form = TipForm(request.POST, instance=tip)
        if form.is_valid():
            form.save()
            return redirect("lista_tips")
    else:
        form = TipForm(instance=tip)
    return render(request, "foodieApp/editar_tip.html", {"form": form})

def eliminar_tip(request, tip_id):
    tip = get_object_or_404(Tip, pk=tip_id)
    if request.method == "POST":
        tip.delete()
        return redirect("lista_tips") 
    return render(request, "foodieApp/eliminar_tip.html", {"tip": tip})

def galeria_imagenes(request):
    imagenes = Imagen.objects.all()
    return render(request, "foodieApp/galeria_imagenes.html", {"imagenes": imagenes})

def agregar_imagen(request):
    if request.method == "POST":
        form = ImagenForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.autor = request.user
            form.save()
            return redirect("galeria_imagenes")
    else:
        form = ImagenForm()
    return render(request, "foodieApp/agregar_imagen.html", {"form": form})

def editar_imagen(request, imagen_id):
    imagen = get_object_or_404(Imagen, pk=imagen_id)
    if request.method == "POST":
        form = ImagenForm(request.POST, request.FILES, instance=imagen)
        if form.is_valid():
            form.save()
            return redirect("galeria_imagenes")
    else:
        form = ImagenForm(instance=imagen)
    return render(request, "foodieApp/editar_imagen.html", {"form": form})

def eliminar_imagen(request, imagen_id):
    imagen = get_object_or_404(Imagen, pk=imagen_id)
    if request.method == "POST":
        imagen.delete()
        return redirect("galeria_imagenes")
    return render(request, "foodieApp/borrar_imagen.html", {"imagen": imagen})

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegistroForm()
    return render(request, "registro.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("home")

def configuracion_usuario(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'configuracion_usuario.html', {'form': form})

def sobre_mi (request):
    return render(request, "foodieApp/sobre_mi.html")