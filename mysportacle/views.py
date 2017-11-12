import datetime
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from ranker.models import Rank
from picks.models import Pick
from gamelist.models import Sport, Game
from leaderboard.models import Leaderboard
from .models import Profile, Relationship

# Create your views here.
def profile_page(request, username):
    user = get_object_or_404(User, username=username)
    
    isFollowing = False
    isOwn = False
    if request.user.is_authenticated():
        currUser = request.user
        
        if user==currUser:
            isOwn = True
        elif Relationship.objects.filter(from_profile=currUser.profile, to_profile=user.profile, status=1).exists():
            isFollowing = True
    
    profile = user.profile
    numFollowing = profile.get_following().count()
    numFollowers = profile.get_followers().count()
    
    tempRank = Rank.objects.filter(user=user).order_by('-updated')
    if tempRank:
        rank = tempRank[0]
        smoothRank = float(rank.smoothRank)
    else:
        rank = None
        smoothRank = 0
        
    tempLeader = Leaderboard.objects.filter(user=user)
    if tempLeader:
        leader = tempLeader[0]
    else:
        leader = None
    
    #pick history
    today = datetime.date.today()
    weekDate = today - datetime.timedelta(days=7)
    monthDate = today - datetime.timedelta(days=30)
    
    current = Pick.objects.filter(user=user, game__outcome="U")
    lastWeek = Pick.objects.filter(user=user, updated__range=[weekDate, today]).exclude(game__outcome="U")
    lastMonth = Pick.objects.filter(user=user, updated__range=[monthDate, today]).exclude(game__outcome="U")
    allTime = Pick.objects.filter(user=user).exclude(game__outcome="U")
    
    progress = int((smoothRank-int(smoothRank))*100)
    
    context = {'user':user, 
    'isOwn':isOwn,
    'isFollowing':isFollowing,
    'numFollowing':numFollowing,
    'numFollowers':numFollowers,
    'leader':leader,
    'progress':progress,
    'current':current,
    'lastWeek':lastWeek,
    'lastMonth':lastMonth,
    'allTime':allTime,}
    
    return render(request, 'mysportacle/profile.html', context)
    
@require_POST
def follow(request, user_id):
    if not request.user.is_authenticated():
        return redirect('/login/')
    
    from_user = request.user
    from_profile = from_user.profile
    to_user = get_object_or_404(User, id=user_id)
    to_profile = to_user.profile
    
    from_profile.add_relationship(to_profile, 1)
    
    return redirect('profile', username=to_user.username)
    
@require_POST
def unfollow(request, user_id):
    if not request.user.is_authenticated():
        return redirect('/login/')
    
    from_user = request.user
    from_profile = from_user.profile
    to_user = get_object_or_404(User, id=user_id)
    to_profile = to_user.profile
    
    from_profile.remove_relationship(to_profile, 1)
    
    return redirect('profile', username=to_user.username)
    
def list_followers(request, username):
    user = get_object_or_404(User, username=username)
    
    profile = user.profile
    followers = profile.get_followers()
    
    title = "Followers"
    relationships = Leaderboard.objects.filter(type="A", user__profile=followers)
    
    context = {'title':title,
    'relationships':relationships}
    
    return render(request, 'mysportacle/relationships.html', context)
    
def list_following(request, username):
    user = get_object_or_404(User, username=username)
    
    profile = user.profile
    following = profile.get_following()
    
    title = "Following"
    relationships = Leaderboard.objects.filter(type="A", user__profile=following)
    
    context = {'title':title,
    'relationships':relationships}
    
    return render(request, 'mysportacle/relationships.html', context)