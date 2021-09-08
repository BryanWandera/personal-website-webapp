from django.shortcuts import render
from .models import PortfolioPiece
from .models import AboutCopy

# CRUD Create Retrieve Update Delete

def portfolio_pieces_list_view(request):
    context = {
        "portfolio_pieces": PortfolioPiece.objects.all(), 
        "about_copy": AboutCopy.objects.all()

    }
    return render(request, "index.html", context)

# def about_copy_view(request):
#     context = {
#         "about_copy": AboutCopy.objects.all()
#     }    
#     return render(request, "index.html", context)
