from django.shortcuts import render
from django.http import HttpResponse




def homepage(request):
    return render(request, "store/index.html")
    
    # return HttpResponse("<h1> Home page")


    

# Create your views here.
