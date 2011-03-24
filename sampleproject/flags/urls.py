from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^test/$', views.test, {'template':'hello.html'}),
)