from pytz import timezone
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import Pick
from cart.cart import Cart
from django.contrib.auth.models import User
from gamelist.models import Game

changes = []
late = []
success = []

def pick_create(request):
    if not request.user.is_authenticated():
        return redirect('/login/')

    now = datetime.now(timezone('UTC'))

    cart = Cart(request)
    if request.method == 'POST':
        for item in cart:
            if item['game'].gameTime > now:
                if Pick.objects.filter(user=request.user, game=item['game']):


                    Pick.objects.filter(user=request.user, game=item['game']).update(selection=item['selection'],
                                             odds=item['selectionOdds'],
                                             probability=item['selectionProb'])

                    changes.append(item)
                else:
                    Pick.objects.create(user=request.user,
                                             game=item['game'],
                                             selection=item['selection'],
                                             odds=item['selectionOdds'],
                                             probability=item['selectionProb']
                                             )

                    success.append(item)
            else:
                late.append(item)


    context = {'success':success, 'late':late, 'changes':changes}

    # clear the cart
    cart.clear()

    return render(request, 'picks/created.html', context)
            
