# webVinilos/views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import Vinilo
from .forms import CSVUploadForm
import pandas as pd

def cargar_datos_bd():
    data = pd.DataFrame(list(Vinilo.objects.all().values()))
    return data

data = cargar_datos_bd()

def inicio(request):
    return render(request, 'inicio.html')

def buscar(request):
    artista = request.GET.get('artist', '')
    album = request.GET.get('album', '')

    if artista and album:
        resultados = Vinilo.objects.filter(artista__icontains=artista, album__icontains=album)
    else:
        resultados = Vinilo.objects.none()

    return render(request, 'resultados.html', {'resultados': resultados})

def catalogo(request):
    vinilos = Vinilo.objects.all()
    return render(request, 'catalogo.html', {'vinilos': vinilos})

def gestor(request):
    global data  # Permite modificar la variable global `data`
    
    if request.method == "POST":
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            archivo_csv = request.FILES['archivo_csv']
            data = pd.read_csv(archivo_csv)  # Actualiza la variable `data` con el nuevo archivo
            
            # Limpiar tabla antes de la nueva carga
            Vinilo.objects.all().delete()

            for _, row in data.iterrows():
                Vinilo.objects.create(
                    artista=row['Artista'],
                    album=row['Album'],
                    estado=row['Estado (disco/caratula)'],
                    precio=row['Precio'],
                    comuna=row['Comuna'],
                    tienda=row['Tienda']
                )

            # Recargar los datos desde la base de datos después de la actualización
            data = cargar_datos_bd()

            messages.success(request, "Datos actualizados correctamente.")
            return redirect('gestor')
    else:
        form = CSVUploadForm()
    
    return render(request, 'gestor.html', {'form': form})

def filtrar_artistas(request):
    query = request.GET.get('q', '').strip()
    if query:
        artistas = Vinilo.objects.filter(artista__icontains=query).values_list('artista', flat=True).distinct()[:4]
        return JsonResponse(list(artistas), safe=False)
    return JsonResponse([], safe=False)
