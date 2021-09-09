from django.shortcuts import render
from .models import PortfolioPiece
from .models import AboutCopy
from django.http import HttpResponse
import requests
import json


encoded_credentials = "MmZjMGI4ZjFhZDM5NDNlZWE0NjlmZWNkNDk1NzdiMmY6Y2QyNWE0OTA2YTEzNDA4Nzg0OThlYTM2MThlZTRhM2U="
spotify_refresh_token ="AQBaVbMxMY9kYSyBeVQP-Uf5NUfbn0nIXm_hAJ8NbHYdgIAZ7eNJ9lvaMiijLrg0lyP3LE79qT6laYpdUeFQNvEO8kVy1Jlmqtvb1TDi_DVdcWWrSGHyfHxUIlJNy5X0LoE"

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

def spotify_playlists_view(request):
    return render(request, "playlists.html")    

def spotify_api(request):
    if request.method == "GET":
        try:
            url = "https://accounts.spotify.com/api/token"
            payload = {'grant_type':'refresh_token', 'refresh_token':spotify_refresh_token}
            headers = {'Authorization': "Basic "+encoded_credentials}
            response = requests.post(url,data=payload,headers=headers)
        except:  
        
            response = json.dumps([{'access_token':'could not get'}])    

    return HttpResponse(response, content_type='text/json')    


# curl -H "Authorization: Basic MmZjMGI4ZjFhZDM5NDNlZWE0NjlmZWNkNDk1NzdiMmY6Y2QyNWE0OTA2YTEzNDA4Nzg0OThlYTM2MThlZTRhM2U=" -d grant_type=refresh_token -d refresh_token=AQBaVbMxMY9kYSyBeVQP-Uf5NUfbn0nIXm_hAJ8NbHYdgIAZ7eNJ9lvaMiijLrg0lyP3LE79qT6laYpdUeFQNvEO8kVy1Jlmqtvb1TDi_DVdcWWrSGHyfHxUIlJNy5X0LoE https://accounts.spotify.com/api/token    