from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductoSerializer
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponse
from io import BytesIO
import openpyxl
import qrcode


class ProductoViewSet(ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

@login_required
def lista_productos(request):
    q = request.GET.get("q")

    productos = Producto.objects.all()

    if q:
        productos = Producto.objects.filter(nombre__icontains=q) | \
                    Producto.objects.filter(codigo__icontains=q)
    else:
        productos = Producto.objects.all()

    return render(request, "inventario/lista.html", {"productos": productos})


@login_required
def crear_producto(request):
    form = ProductoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("lista_productos")
    return render(request, "inventario/form.html", {"form": form})

@login_required
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    form = ProductoForm(request.POST or None, instance=producto)
    if form.is_valid():
        form.save()
        return redirect("lista_productos")
    return render(request, "inventario/form.html", {"form": form})

@login_required
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect("lista_productos")

@login_required
def dashboard(request):
    productos = Producto.objects.all()

    total_productos = productos.count()
    bajo_stock = productos.filter(cantidad__lt=5).count()
    ultimos = productos.order_by('-id')[:5]

    contexto = {
        'total': total_productos,
        'bajo': bajo_stock,
        'ultimos': ultimos
    }
    return render(request, "inventario/dashboard.html", contexto)

@login_required
def exportar_excel(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Inventario"

    ws.append(["ID", "Nombre", "Código", "Cantidad", "Ubicación"])

    for p in Producto.objects.all():
        ws.append([p.id, p.nombre, p.codigo, p.cantidad, p.ubicacion])

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="inventario.xlsx"'

    wb.save(response)
    return response

@login_required
def qr_producto(request, pk):
    url = request.build_absolute_uri(f"/producto/{pk}/")

    qr = qrcode.make(url)

    buffer = BytesIO()
    qr.save(buffer, format="PNG")

    return HttpResponse(buffer.getvalue(), content_type="image/png")

@login_required
def detalle_producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    return render(request, "inventario/detalle.html", {
        "producto": producto
    })

    
  
