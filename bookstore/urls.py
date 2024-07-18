
from django.urls import path
from .import views
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('addbook', views.addbook_view, name='addbook'),
    path('viewbook', views.viewbook_view),
    path('addfile', views.addfile, name='addfile'),
    path('dictionary', views.dictionary, name='dictionary'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)