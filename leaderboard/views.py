from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from leaderboard.models import Leaderboard

def leaderboard_page(request):
    lastWeek = Leaderboard.objects.filter(type="W").order_by('-edge')[:100]
    lastMonth = Leaderboard.objects.filter(type="M").order_by('-edge')[:100]
    allTime = Leaderboard.objects.filter(type="A").order_by('-edge')[:100]
    
    return render(request, 'leaderboard/leaderboard.html', {'lastWeek':lastWeek, 'lastMonth':lastMonth, 'allTime':allTime})
    
    