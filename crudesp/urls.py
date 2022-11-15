from xml.dom.minidom import Document
from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns=[ 
    path('',views.inicio,name='inicio'),
    path('nosotros',views.nosotros, name='nosotros'),
    #interfaz de creacion
    path('emp',views.emp, name='emp'),
    path('empleados',views.empleados, name='emple'),
    path('emp/crear',views.crearemp, name='crear'),
    path('emp/editar',views.editaremp, name='editar'),
    path('eliminar/<int:id>',views.eliminar, name='eliminar'),
    path('emp/editar/<int:id>',views.editaremp, name='editar')
    


# ahi se agrega lo siguiente para las imagenes
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)