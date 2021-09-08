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


def battlecreek_design_view(request):
    return render(request, "battlecreek-design.html")

def airbus_design_view(request):
    return render(request, "airbus-design.html")

def twentyeight_design_view(request):
    return render(request, "twenty-eight-design.html")    