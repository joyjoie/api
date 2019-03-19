from django.conf.urls import url ,include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^project/(\d+)',views.project,name ='project'),
    url(r'^profile',views.my_profile, name='myprofile'),
    url(r'^profile/(\d+)?$', views.profile, name='profile'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^profileapi', views.ProfileList.as_view()),
    url(r'^projectapi', views.ProjectList.as_view()),
    url(r'^search/', views.search, name='search'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)