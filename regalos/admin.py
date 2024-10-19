import random
from django.contrib import admin
from .models import Participante

@admin.action(description='Asignar amigos secretos aleatoriamente')
def asignar_amigos_secretos(modeladmin, request, queryset):
    participantes = list(queryset)
    random.shuffle(participantes)

    for i, participante in enumerate(participantes):
        siguiente = participantes[(i + 1) % len(participantes)]
        participante.amigo_secreto = siguiente
        participante.save()

@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'amigo_secreto']
    actions = [asignar_amigos_secretos]
