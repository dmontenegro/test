from django.conf.urls import patterns, url, include
from customers.views import TenantView
#from inventories.views import CreateInventoryView

urlpatterns = patterns('',
    #url(r'^$', TenantView.as_view(), name='index'),
    url(r'^' , include('inventories.urls', namespace='inventories')),
    url(r'^books_cbv/' , include('books_cbv.urls', namespace='books_cbv')),
)
