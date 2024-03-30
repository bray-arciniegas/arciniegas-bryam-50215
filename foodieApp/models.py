from django.db import models
from django.contrib.auth.models import User

class Receta(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    ingredientes = models.TextField()
    instrucciones = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='media/imagenes_recetas/')

    def __str__(self):
        return self.titulo

class Tip(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()

    def __str__(self):
        return self.titulo

class Imagen(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='media/galeria/')

    def __str__(self):
        return f"Imagen de {self.autor.username}"

class Coctel(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    ingredientes = models.TextField()
    instrucciones = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='media/imagenes_recetas/')

    def __str__(self):
        return self.titulo

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="media/avatars/", default="media/avatars/default_avatar.png")

    def __str__(self):
        return self.user.username