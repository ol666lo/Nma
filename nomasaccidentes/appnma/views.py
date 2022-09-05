from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from .models import VistaClientes

# Create your views here.
@login_required(login_url='/accounts/login/')
def home (request):
    vistaClientess = VistaClientes.objects.all()
    data = { 
        'vistaClientess': vistaClientess
    }
 
    return render(request, 'appnma/home.html',data)