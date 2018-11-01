from django.shortcuts import render
from django.views import generic
from .models import Departamento,Software

# Create your views here.
def index(request):
    return render(request,"index.html")


class createSoft(generic.CreateView):
    template_name = "createSoft.html"
    model = Software

    fields = ["nombreSoftware", "funcion","departamento"]
    success_url = "/index/"

class createDepa(generic.CreateView):
    template_name = "createDepa.html"
    model = Departamento
    fields = ["depa"]
    success_url = "/index/"

class listSoft(generic.ListView):
    template_name = "listSoft.html"
    model = Software
    fields = ["nombreSoftware", "funcion","departamento"]
