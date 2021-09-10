"""personalwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysite.views import portfolio_pieces_list_view
from mysite.views import battlecreek_design_view
from mysite.views import airbus_design_view
from mysite.views import twentyeight_design_view
from mysite.views import spotify_playlists_view
from mysite.views import spotify_api
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portfolio_pieces_list_view),
    path('battlecreek-design', battlecreek_design_view), 
    path('airbus-design', airbus_design_view),
    path('twentyeight-design', twentyeight_design_view),
    path('playlists', spotify_playlists_view ),
    path('spotifyapi', spotify_api),  
    path('playlists-final', TemplateView.as_view(template_name='index.html'))


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)