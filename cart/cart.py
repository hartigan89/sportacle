from decimal import Decimal
from django.conf import settings
from gamelist.models import Game


class Cart(object):

    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(1 for game in self.cart.values())

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products from the database.
        """
        game_ids = self.cart.keys()
        # get the product objects and add them to the cart
        games = Game.objects.filter(id__in=game_ids)
        for game in games:
            self.cart[str(game.id)]['game'] = game

        for item in self.cart.values():
            item['selectionOdds'] = Decimal(item['selectionOdds'])
            item['selectionProb'] = Decimal(item['selectionProb'])
            yield item

    def add(self, game, selection):
        """
        Add a product to the cart or update its quantity.
        """
        game_id = str(game.id)
        
        if selection == "V":
            selectionOdds = str(game.visitorOdds)
            selectionProb = str(round((1/game.visitorOdds)/((1/game.visitorOdds)+(1/game.homeOdds)), 6))
                
        elif selection == "H":
            selectionOdds = str(game.homeOdds)
            selectionProb = str(round((1/game.homeOdds)/((1/game.visitorOdds)+(1/game.homeOdds)), 6))
        
        if game_id not in self.cart:
            self.cart[game_id] = {'selection': selection, 'selectionOdds': selectionOdds, 'selectionProb': selectionProb}
        else:
            self.cart[game_id]['selection'] = selection
            self.cart[game_id]['selectionOdds'] = selectionOdds
            self.cart[game_id]['selectionProb'] = selectionProb
        
        self.save()

    def switch(self, game):
        """
        Switch the user's selection.
        """
        game_id = str(game.id)
        if game_id in self.cart:
            selection = self.cart[game_id]['selection']
            if selection == "V":
                self.cart[game_id]['selection'] = "H"
            else:
                self.cart[game_id]['selection'] = "V"

            self.save()

    def remove(self, game):
        """
        Remove a product from the cart.
        """
        game_id = str(game.id)
        if game_id in self.cart:
            del self.cart[game_id]
            self.save()

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def clear(self):
        # empty cart
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True
