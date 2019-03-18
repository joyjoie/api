from django.conf.urls import url ,include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^$',views.my_project,name='myprojects')
    url(r'^image/(\d+)',views.image,name ='image'),
    url(r'^profile',views.my_profile, name='myprofile'),
    url(r'^profile/(\d+)?$', views.profile, name='profile'),
    url(r'^upload/$', views.upload, name='upload'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)