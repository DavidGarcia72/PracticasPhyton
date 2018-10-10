from django.shortcuts import render
from .models import Tweet
# Create your views here.

def index(request):
    context={"value": "Que pedo que pex exdi", "object": Tweet.objects.get(id=2)}
    return render(request,"tweet/index.html",context)
