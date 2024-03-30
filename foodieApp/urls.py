from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("sobremi/", sobre_mi, name="sobremi"),
    path("recetario/", recetario, name="recetario"),
    path("recetas/<int:receta_id>/", detalle_receta, name="detalle_receta"),
    path("agregar_receta/", agregar_receta, name="agregar_receta"),
    path("editar_receta/<int:receta_id>/", editar_receta, name="editar_receta"),
    path("eliminar_receta/<int:receta_id>/", eliminar_receta, name="eliminar_receta"),
    path("coctelero/", coctelero, name="coctelero"),
    path("cocteles/<int:coctel_id>/", detalle_coctel, name="detalle_coctel"),
    path("agregar_coctel/", agregar_coctel, name="agregar_coctel"),
    path("editar_coctel/<int:coctel_id>/", editar_coctel, name="editar_coctel"),
    path("eliminar_coctel/<int:coctel_id>/", eliminar_coctel, name="eliminar_coctel"),
    path("tips/", lista_tips, name="lista_tips"),
    path("agregar_tip/", agregar_tip, name="agregar_tip"),
    path("editar_tip/<int:tip_id>/", editar_tip, name="editar_tip"),
    path("eliminar_tip/<int:tip_id>/", eliminar_tip, name="eliminar_tip"),
    path("galeria/", galeria_imagenes, name="galeria_imagenes"),
    path("agregar_imagen/", agregar_imagen, name="agregar_imagen"),
    path("editar_imagen/<int:imagen_id>/", editar_imagen, name="editar_imagen"),
    path("eliminar_imagen/<int:imagen_id>/", eliminar_imagen, name="eliminar_imagen"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", logout_view, name="logout"),
    path("registro/", registro, name="registro"),
    path('configuracion-usuario/', configuracion_usuario, name='configuracion_usuario'),
]
