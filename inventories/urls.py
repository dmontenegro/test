from django.conf.urls import patterns, url, include
from .views import Registrarse
from inventories import views

urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login', {'template_name':'index_login.html'}, name='login'),
    url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^registrarse/$', Registrarse.as_view(), name='registrarse'),
    url(r'^books_cbv/' , include('books_cbv.urls', namespace='books_cbv')),

)