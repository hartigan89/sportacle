import numpy as np
import scipy.stats as sp
from poibin import PoiBin

def getRank(numGames, p, currRank):
    trueRank = 0
    smoothRank = 0
    rank = "Unranked"
    
    #set smoothing factor
    smooth = 0.2
    
    #p-value boundaries
    pBound = []
    pBound.append(sp.norm(0,1).cdf(2.5))
    pBound.append(sp.norm(0,1).cdf(2.0))
    pBound.append(sp.norm(0,1).cdf(1.5))
    pBound.append(sp.norm(0,1).cdf(1.0))
    pBound.append(sp.norm(0,1).cdf(0.5))
    pBound.append(sp.norm(0,1).cdf(0.0))
    pBound.append(sp.norm(0,1).cdf(-0.5))
    pBound.append(sp.norm(0,1).cdf(-1.0))
    pBound.append(sp.norm(0,1).cdf(-1.5))
    pBound.append(sp.norm(0,1).cdf(-2.0))
    pBound.append(sp.norm(0,1).cdf(-2.5))
    
    if numGames < 10:
        rank = "Unranked"
        trueRank = 0
        smoothRank = 0
    else:
        #get p-value rank
        if p > pBound[0]:
            trueRank = 0
        elif p > pBound[1]:
            trueRank = 1 + (p-pBound[0])/(pBound[1]-pBound[0])
        elif p > pBound[2]:
            trueRank = 2 + (p-pBound[1])/(pBound[2]-pBound[1])
        elif p > pBound[3]:
            trueRank = 3 + (p-pBound[2])/(pBound[3]-pBound[2])
        elif p > pBound[4]:
            trueRank = 4 + (p-pBound[3])/(pBound[4]-pBound[3])
        elif p > pBound[5]:
            trueRank = 5 + (p-pBound[4])/(pBound[5]-pBound[4])
        elif p > pBound[6]:
            trueRank = 6 + (p-pBound[5])/(pBound[6]-pBound[5])
        elif p > pBound[7]:
            trueRank = 7 + (p-pBound[6])/(pBound[7]-pBound[6])
        elif p > pBound[8]:
            trueRank = 8 + (p-pBound[7])/(pBound[8]-pBound[7])
        elif p > pBound[9]:
            trueRank = 9 + (p-pBound[8])/(pBound[9]-pBound[8])
        elif p > pBound[10]:
            trueRank = 10 + (p-pBound[9])/(pBound[10]-pBound[9])
        else:
            trueRank = 11
    
        #if # of games played is greated than 30 then smooth the ranks
        if numGames > 10:
            smoothRank = currRank + (trueRank-currRank)*smooth
        
        if smoothRank < 1:
            rank = "Donkey I"
        elif smoothRank < 2:
            rank = "Donkey II"
        elif smoothRank < 3:
            rank = "Donkey III"
        elif smoothRank < 4:
            rank = "Amateur I"
        elif smoothRank < 5:
            rank = "Amateur II"
        elif smoothRank < 6:
            rank = "Amateur III"
        elif smoothRank < 7:
            rank = "Veteran I"
        elif smoothRank < 8:
            rank = "Veteran II"
        elif smoothRank < 9:
            rank = "Veteran III"
        elif smoothRank < 10:
            rank = "Expert I"
        elif smoothRank < 11:
            rank = "Expert II"
        else:
            rank = "Expert III"

    return {'trueRank':trueRank, 'smoothRank':smoothRank, 'rank':rank}