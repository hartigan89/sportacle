from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from ranker.models import Rank

TYPE_CHOICES = (
        ('W', 'Weekly'),
        ('M', 'Monthly'),
        ('A', 'All Time')
    )

class Leaderboard(models.Model):
    user = models.ForeignKey(User)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    numGames = models.IntegerField()
    gamesWon = models.IntegerField()
    expWon = models.DecimalField(max_digits=10, decimal_places=6)
    edge = models.DecimalField(max_digits=10, decimal_places=6)
    pValue = models.DecimalField(max_digits=10, decimal_places=6)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    @property
    def getRank(self):
        tempRank = Rank.objects.filter(user=self.user).order_by('-updated')
        if tempRank:
            currRank = tempRank[0].rank
        else:
            currRank = "Unranked"
        
        return currRank
    
    @property
    def getWinRate(self):
        if self.numGames > 0:
            winRate = (float(self.gamesWon) / float(self.numGames))*100
        else:
            winRate = 0.0
        
        return winRate
        
    @property
    def getExpRate(self):
        if self.numGames > 0:
            expRate = (float(self.expWon) / float(self.numGames))*100
        else:
            expRate = 0.0
        
        return expRate
        
    @property
    def formatEdge(self):
        edge = float(self.edge) * 100
        
        return edge
    
    class Meta:
        ordering = ('type', '-edge')
    
    
