import numpy as np
import scipy.stats as sp
from poibin import PoiBin

def getStats(prob, gamesWon):
    numGames = len(prob)
    expWon = 0
    edge = 0
    p = 0
    
    if numGames > 0:
        #get p-value
        pb = PoiBin(prob)
        
        if gamesWon > 0:
            p = 1-pb.cdf(gamesWon-1)
        else:
            p = 1-pb.cdf(gamesWon)
            
        #get expected number of games won
        expWon = sum(prob)
        
        #get probability edge
        edge = (gamesWon-expWon)/numGames

    return {'numGames':numGames, 'expWon':expWon, 'edge':edge, 'p':p}