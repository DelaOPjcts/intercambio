from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Participante(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    amigo_secreto = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.usuario.username  # Muestra el nombre del usuario como representación del participante

# Señal para crear automáticamente un participante cuando se crea un usuario
@receiver(post_save, sender=User)
def crear_participante(sender, instance, created, **kwargs):
    if created:
        Participante.objects.create(usuario=instance)

class Regalo(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)  # Cada regalo pertenece a un participante
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='regalos/', null=True, blank=True)
    enlace1 = models.URLField(blank=True)
    enlace2 = models.URLField(blank=True)
    enlace3 = models.URLField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo