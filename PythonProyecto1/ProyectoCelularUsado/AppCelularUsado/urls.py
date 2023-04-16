from django.urls import path
from AppCelularUsado import views
from django.contrib.auth.views import LogoutView


# app_name = 'AppCelularUsado'

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('celular', views.celular, name='Celular'), 
    path('usuario', views.usuario, name='Usuario'),
    path('comentarios', views.comentarios, name='Comentarios'),
    path('agregarProducto', views.agregarProducto, name='AgregarProducto'),
    path('crearUsuario', views.crearUsuario, name='CrearUsuario'),
    path('usuarioCreadoExito', views.usuarioCreadoExito, name='UsuarioCreadoExito'),
    path('buscarCelular', views.buscarCelular, name='BuscarCelular'),
    path('buscar/', views.buscar),
    path('mostrarCelulares', views.mostrarCelulares, name='MostrarCelulares'),
    path('eliminarProducto/<o_nombre>', views.eliminarProducto, name='EliminarProducto'),
    path('editarProducto/<producto_nombre>', views.editarProducto, name='EditarProducto'),

    path('producto/list', views.ProductoList.as_view(), name='List'),
    path('<int:pk>', views.ProductoDetalle.as_view(), name='Detail' ),
    path('nuevo', views.ProductoCreacion.as_view(), name='New' ),
    path('editar/<int:pk>', views.ProductoUpdate.as_view(), name='Edit' ),
    path('borrar/<int:pk>', views.ProductoDelete.as_view(), name='Delete' ),
    path('login', views.login_request, name='Login'),
    path('register', views.register, name='Registro'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='Logout'),

    path('carrito', views.carrito, name='Carrito'),
    path('acercaDeMi', views.acercaDeMi , name='AcercaDeMi'),
    path('editarPerfil', views.editarPerfil , name='EditarPerfil'),
    path('agregarAvatar', views.agregarAvatar , name='AgregarAvatar'),

    


    


    # path('resultadosPorBusqueda', views.resultadosPorBusqueda),
]