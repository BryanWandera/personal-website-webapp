
from django.contrib import admin
from django.urls import path
from mysite.views import portfolio_pieces_list_view
from mysite.views import battlecreek_design_view
from mysite.views import airbus_design_view
from mysite.views import twentyeight_design_view
from mysite.views import spotify_api
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404


handler404 = 'mysite.views.handler404'
handler500 = 'mysite.views.handler500'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portfolio_pieces_list_view),
    path('battlecreek-design', battlecreek_design_view), 
    path('airbus-design', airbus_design_view),
    path('twentyeight-design', twentyeight_design_view),   
    path('spotifyapi', spotify_api),  
    path('playlists', TemplateView.as_view(template_name='index.html')),
    
  


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)