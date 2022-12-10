from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacto', views.contact, name='contact'),
    path('empresa', views.empresa, name='empresa'),
    # /categoria/calzados-deportivos
    re_path(r'^categoria/(?P<name>[-\w]+)$', views.category, name='categoria'),
    re_path(r'^descripcion/(?P<producto>[-\w]+)$', views.descripcion, name='descripcion'),
    path('oferta', views.oferta, name='oferta'),
]
