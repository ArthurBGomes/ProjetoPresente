from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from .models import Gamificacao, UsuarioGamificacao

User = get_user_model()


@receiver(post_save, sender=User)
def dar_trilha_inicial(sender, instance, created, **kwargs):
    if created:
        try:
            gamificacao_inicial = Gamificacao.objects.get(titulo="Hello World")

            UsuarioGamificacao.objects.create(
                user=instance,
                gamificacao=gamificacao_inicial
            )

        except Gamificacao.DoesNotExist:
            pass