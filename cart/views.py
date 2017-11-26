from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from gamelist.models import Game
from .cart import Cart

@require_POST
def cart_add(request, game_id):
    cart = Cart(request)
    game = get_object_or_404(Game, id=game_id)
    
    if 'visitor' in request.POST:
        cart.add(game=game, selection='V')
    elif 'home' in request.POST:
        cart.add(game=game, selection='H')
        
    return redirect('cart:cart_detail')

def cart_switch(request, game_id):
    cart = Cart(request)
    game = get_object_or_404(Game, id=game_id)
    cart.switch(game)
    return redirect('cart:cart_detail')

def cart_remove(request, game_id):
    cart = Cart(request)
    game = get_object_or_404(Game, id=game_id)
    cart.remove(game)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
