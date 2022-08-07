from django.shortcuts import render
from store.models import Product

def home(request):
    products = Product.objects.all().filter(is_available=True)

    context = {                     #Creamos este diccionario para enviarlo a la pagina mediante el render(linea 12)
        "products": products,
    }
    

    return render(request,"home.html", context)

