"""WebDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from DjangoApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', views.log_in, name='login'),
    path('logout', views.log_out, name='logout'),
    path('registro', views.registro, name="registro"),
    path('',views.index, name="index"),
    path('servicios',views.servicios, name="servicios"),
    path('portfolio',views.portfolio, name="portfolio"),
    path('blog',views.blog, name="blog"),
    path('blogSingle',views.comentarios, name="comentarios"),
    path('agregarServicio', views.agregarServicio, name="agregarServicio"),
    path('crearPost', views.crearPost, name="crearPost"),
    path('blogSingle/<post_id>/', views.blogSingle, name="blogSingle"),
    path('acerca', views.acerca, name="acerca"),
    path('eliminarPost/<post_id>/', views.eliminarPost, name="eliminarPost"),
    path('editarPost/<post_id>/', views.editarPost, name="editarPost"),
    path('perfil',views.perfil, name="perfil"),
    path('editarPerfil',views.editarPerfil, name="editarPerfil"),
    path('avatar',views.avatar, name="avatar")
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
