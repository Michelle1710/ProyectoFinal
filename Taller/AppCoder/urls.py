from django.urls import path

from AppCoder import views
from AppCoder.views import servicios
from Taller.AppCoder.views import ServicioDelete, ServicioDetail, ServicioList, crear_cliente, crear_rev, editar_revision, editar_usuario, eliminar_revision,eliminar_usuario, revision

urlpatterns = [

    path('', inicio, name="inicio"),

    path('servicios/', servicios, name="servicios"),
    path('crear_usuario/', crear_cliente, name="crear_usuario"),
    path('eliminar_usuario/<placa>', eliminar_usuario, name="eliminar_usuario"),
    path('editar_estudiante/<estudiante_id>', editar_usuario, name="editar_usuario"),

    path('servicio/list', ServicioList.as_view(), name="servicio_list"),
    path(r'^(?P<pk>\d+)$', ServicioDetail.as_view(), name="servicio_detail"),
    path(r'^nuevo$', ServicioDetail.as_view(), name="servicioe_create"),
    path(r'^editar/(?P<pk>\d+)$', ServicioDetail.as_view(), name="servicio_update"),
    path(r'^eliminar/(?P<pk>\d+)$', ServicioDelete.as_view(), name="servicio_delete"),


    path('revision/', revision, name="revision"),
    path('crear_revision/', crear_rev, name="crear_revision"),
    path('eliminar_curso/<curso_id>/', eliminar_revision, name="eliminar_revision"),
    path('editar_curso/<curso_id>/', editar_revision, name="editar_revision"),
   
]
