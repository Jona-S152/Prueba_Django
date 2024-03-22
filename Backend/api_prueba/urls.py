
from rest_framework.documentation import include_docs_urls
from django.urls import path
from . import views
 
urlpatterns = [
    path('crear/', views.crear, name='crear'),
    path('listar/', views.listar, name='listar'),
    path('actualizar/<int:id>/', views.actualizar, name='actualizar'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('buscar/<int:id>/', views.buscar, name='buscar')
]