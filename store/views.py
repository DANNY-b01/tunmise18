from django.shortcuts import render
from django.http import HttpResponse
# from .forms import productiom
from .models import product




def homepage(request):
    all_products=product.objects.all()
    context={"all_products": all_products}
    return render(request, "store/index.html", context)
def detailpage(request, input_id):
    current_product = product.objects.get(id=input_id)
    context={"current_product": current_product}
    return render(request, "store/detail.html", context)


    
    # return HttpResponse("<h1> Home page")


    

# Create your views here.
