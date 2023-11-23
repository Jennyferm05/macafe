from django.contrib import messages
from django.shortcuts import render, redirect
from .form import VentaForm
from .models import Venta


def inicio(request):
    return render(request, 'paginas/inicio.html', {'section': 'inicio'})


def registrar_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form = form.save()
            messages.success(request, 'Venta Registrada con exito!')
            return redirect('ventas')
    else:
        form = VentaForm()

    return render(request, 'paginas/registrar_venta.html', {'form': form})



def ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'paginas/ventas.html', {'ventas': ventas})
