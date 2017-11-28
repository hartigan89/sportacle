from django.shortcuts import render
from leaderboard.models import Leaderboard

def leaderboard_page(request):
    lastWeek = Leaderboard.objects.filter(type="W").order_by('-pValue')[:100]
    lastMonth = Leaderboard.objects.filter(type="M").order_by('-pValue')[:100]
    allTime = Leaderboard.objects.filter(type="A").order_by('-pValue')[:100]
    
    return render(request, 'leaderboard/leaderboard.html', {'lastWeek':lastWeek, 'lastMonth':lastMonth, 'allTime':allTime})
    
    