from __future__ import absolute_import, unicode_literals
from celery import shared_task
from ranker.ranker import getRank
from django.contrib.auth.models import User
from ranker.models import Rank
from leaderboard.models import Leaderboard

@shared_task()
def update_ranks():
    users = User.objects.all()
    for u in users:
        tempRank = Rank.objects.filter(user=u).order_by('-updated')
        if tempRank:
            currSmoothRank = float(tempRank[0].smoothRank)
            lastUpdate = int(tempRank[0].numGames)
        else:
            currSmoothRank = 0

        stats = Leaderboard.objects.filter(user=u, type="A")[0]
        numGames = stats.numGames
        pValue = stats.pValue

        if numGames != lastUpdate:
            dict = getRank(numGames, pValue, currSmoothRank)

            trueRank = dict["trueRank"]
            smoothRank = dict["smoothRank"]
            rank = dict["rank"]

            Rank.objects.create(user=u,
                                numGames=numGames,
                                trueRank=trueRank,
                                smoothRank=smoothRank,
                                rank=rank,
                                )
