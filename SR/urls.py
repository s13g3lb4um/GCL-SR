from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.sr_list, name='sr_list'),
    url(r'^#Explore$', views.sr_list, {'tab': 'Explore'}, name='sr_list'),
    url(r'^#Create$', views.sr_list, {'tab': 'Create'}, name='sr_list'),
    url(r'^#Visualize$', views.sr_list, {'tab': 'Visualize'}, name='sr_list'),
    url(r'^sr/(?P<item_id>[0-9]+)/$', views.sr_detail, name='sr_detail'),
    url(r'^sr/(?P<item_id>[0-9]+)/analyzed/$', views.analyze_audio, name='analyze_audio'),
    url(r'^sr/(?P<item_id>[0-9]+)/removed/$', views.sr_remove, name='sr_remove') 
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
