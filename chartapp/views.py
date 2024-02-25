from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def index(request):
    products = Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            expense = form.cleaned_data['expense']
            
            # Check if the category already exists
            existing_product = Product.objects.filter(category=category).first()
            if existing_product:
                # If the category exists, update the expense
                existing_product.expense += expense
                existing_product.save()
            else:
                # If the category doesn't exist, create a new entry
                form.save()

            return redirect('index')
    else:
        form = ProductForm()        

    context = {
        "products": products,
        "form": form
    }

    return render(request, 'chartapp/index.html', context)
