from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductForm
from .models import product




def homepage(request):
    all_products=product.objects.all()
    context={"all_products": all_products}
    return render(request, "store/index.html", context)


def detailpage(request, input_id):
    current_product = product.objects.get(id=input_id)
    context={"current_product": current_product}
    return render(request, "store/detail.html", context)


def createproductpage(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return HttpResponse("something went wrong")
    else:
        form=ProductForm()
    context={"form":form}
    return render(request,"store/create_production.html",context)




    
    # return HttpResponse("<h1> Home page")


    

# Create your views here.
