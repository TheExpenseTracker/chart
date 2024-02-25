from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def index(request):
    products = Product.objects.all().order_by('date')

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            expense = form.cleaned_data['expense']
            date = form.cleaned_data['date']  # Extract date from the form
            
            # Check if a product with the same category and date exists
            existing_product = Product.objects.filter(category=category, date=date).first()
            if existing_product:
                # If the product exists, update the expense
                existing_product.expense += expense
                existing_product.save()
            else:
                # If the product doesn't exist, create a new entry
                form.save()

            return redirect('index')
    else:
        form = ProductForm()        

    context = {
        "products": products,
        "form": form
    }

    return render(request, 'chartapp/index.html', context)
