from django.db import models
from gamelist.models import Game
from django.contrib.auth.models import User

PICK_CHOICES = (
        ('V', 'Visitor'),
        ('H', 'Home'),
    )

class Pick(models.Model):
    user = models.ForeignKey(User)
    game = models.ForeignKey(Game)
    selection = models.CharField(max_length=1, choices=PICK_CHOICES)
    odds = models.DecimalField(max_digits=10, decimal_places=2)
    probability = models.DecimalField(max_digits=10, decimal_places=6)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.id)

