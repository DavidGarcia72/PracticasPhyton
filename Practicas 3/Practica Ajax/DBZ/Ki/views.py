from django.shortcuts import render
from django.shortcuts import render
from django.views import generic
from .models import Ki
# from .forms import FormCreate
# Create your views here.

class listTweets(generic.ListView):
    template_name = "tweet/list_tweet.html"
    model = Ki

class detailTweets(generic.DetailView):
    template_name = "tweet/detail.html"
    model = Ki

def detail_tweets(request,id=1):
    quetyset=Ki.objects.get(id=id)
    context={"ki":quetyset}
    return render(request,"tweet/detail.html",context)

class Create(generic.CreateView):
    template_name = "tweet/create.html"
    model = Ki
    fields = ["habilidad"]
    success_url = "/list_tweets/"

# def create(request):
#     form = FormCreate(request.POST or None)
#     if request.POST:
#         if form.is_valid():
#             form.save()
#     else:
#         form=FormCreate(request.POST or None)
#     context={
#     "form": form
#     }
#     return render(request,"tweet/create.html",context)

class updateTweet(generic.UpdateView):
    template_name= "tweet/update.html"
    model = Ki
    fields = ['habilidad']
    success_url = "/list_tweets/"

class deleteTweet(generic.DeleteView):
    template_name= "tweet/delete.html"
    model = Ki
    success_url = "/list_tweets/"
