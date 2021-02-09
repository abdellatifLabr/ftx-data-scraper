from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Spread
from .schema.subscriptions import SpreadSubscription


@receiver(post_save, sender=Spread)
def on_spread_created(sender, instance, created, **kwargs):
    if not created:
        return

    spread = instance
    SpreadSubscription.broadcast(
        group=f'spreads@{spread.pair.id}',
        payload=spread
    )
