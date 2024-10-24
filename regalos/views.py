from django.shortcuts import render
from .models import Participante
from django.shortcuts import redirect
from django.forms import ModelForm
from .models import Regalo
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    # Obtener el participante que está actualmente logueado
    participante = Participante.objects.get(usuario=request.user)
    
    # Obtener el amigo secreto del participante
    amigo_secreto = participante.amigo_secreto

    # Pasar el amigo secreto a la plantilla junto con el participante
    context = {
        'participante': participante,
        'amigo_secreto': amigo_secreto
    }

    return render(request, 'home.html', context)
@login_required(login_url='/login/')
def opciones_regalo(request):
    # Obtener el participante actual
    participante = Participante.objects.get(usuario=request.user)
    
    # Obtener las opciones de regalo de ese participante
    regalos = participante.regalo_set.all()

    context = {
        'regalos': regalos
    }

    return render(request, 'opciones_regalo.html', context)

# Crear un formulario basado en el modelo Regalo
class RegaloForm(ModelForm):
    class Meta:
        model = Regalo
        fields = ['titulo', 'descripcion', 'imagen', 'enlace1', 'enlace2', 'enlace3']

def form_regalo(request):
    participante = Participante.objects.get(usuario=request.user)
    
    if request.method == 'POST':
        form = RegaloForm(request.POST, request.FILES)  # Soporte para subir archivos
        if form.is_valid():
            nuevo_regalo = form.save(commit=False)
            nuevo_regalo.participante = participante
            nuevo_regalo.save()
            return redirect('opciones_regalo')
    else:
        form = RegaloForm()

    return render(request, 'form_regalo.html', {'form': form})

@login_required(login_url='/login/')
def ver_regalo(request, regalo_id):
    regalo = Regalo.objects.get(id=regalo_id)
    es_propio = regalo.participante.usuario == request.user

    if request.method == 'POST':
        form = RegaloForm(request.POST, request.FILES, instance=regalo)
        if form.is_valid():
            form.save()
            return redirect('opciones_regalo')
    else:
        form = RegaloForm(instance=regalo)

    context = {
        'regalo': regalo,
        'form': form,
        'es_propio': es_propio
    }

    return render(request, 'ver_regalo.html', context)

@login_required(login_url='/login/')
def editar_regalo(request, regalo_id):
    regalo = get_object_or_404(Regalo, id=regalo_id)
    
    # Solo el dueño del regalo puede editarlo
    if regalo.participante.usuario != request.user:
        return redirect('opciones_regalo')  # Redirigir si no es el propietario

    if request.method == 'POST':
        form = RegaloForm(request.POST, request.FILES, instance=regalo)
        if form.is_valid():
            form.save()
            return redirect('opciones_regalo')
    else:
        form = RegaloForm(instance=regalo)

    return render(request, 'form_regalo.html', {'form': form})


@login_required(login_url='/login/')
def eliminar_regalo(request, regalo_id):
    regalo = get_object_or_404(Regalo, id=regalo_id, participante__usuario=request.user)
    regalo.delete()
    return redirect('opciones_regalo')
