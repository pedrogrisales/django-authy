
import views
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    
    url(r'^login/$', views.login_user),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    
)

