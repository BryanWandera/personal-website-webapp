from django.shortcuts import render
from .models import PortfolioPiece

# CRUD Create Retrieve Update Delete

def portfolio_pieces_list_view(request):
    context = {
        "portfolio_pieces": PortfolioPiece.objects.all() 

    }
    return render(request, "index.html", context)
