from django.shortcuts import render
from django.views import generic
from .models import Investigacion
# Create your views here.

class createInvs(generic.CreateView):
    template_name = "create.html"
    model = Investigacion
    fields = ["autor", "titulo","content","categoria"]
    success_url = "/index/"

def index(request):
    return render(request,"index.html")

def buscar(request):
    context={"value": "oa",}
    return render(request,"consulta.html",context)

class listCiCom(generic.ListView):
    template_name = "ciCom.html"
    model = Investigacion

class listCiTi(generic.ListView):
    template_name = "ciTi.html"
    model = Investigacion

class listCiNa(generic.ListView):
    template_name = "ciNa.html"
    model = Investigacion

class listCiSo(generic.ListView):
    template_name = "ciSo.html"
    model = Investigacion

class listCiMe(generic.ListView):
    template_name = "ciMe.html"
    model = Investigacion
