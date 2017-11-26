from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Rank(models.Model):
    user = models.ForeignKey(User)
    numGames = models.IntegerField()
    trueRank = models.DecimalField(max_digits=10, decimal_places=6)
    smoothRank = models.DecimalField(max_digits=10, decimal_places=6)
    rank = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def isSVP(self):
        if self.smoothRank > 10:
            return True
        else:
            return False

    class Meta:
        ordering = ('-updated',)