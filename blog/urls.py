from django.urls import path
from .views import render_posts, post_detail

app_name = "blog"  # Nombre del espacio de nombres para la aplicación

urlpatterns = [
    path("", render_posts, name="posts"),  # Ruta para mostrar la lista de posts
    path(
        "<int:post_id>/", post_detail, name="post_detail"
    ),  # Ruta para el detalle del post
]
