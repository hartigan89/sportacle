from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from application.forms import RegistrationForm
from application.models import Sport, Game

# Create your views here.
def GameList(request, sport_slug=None):
    sport = None
    sports = Sport.objects.all()
    games = Game.objects.all()
    if sport_slug:
        sport = get_object_or_404(Sport, slug=sport_slug)
        games = games.filter(sport=sport)
    return render(request, 'application/gamelist.html', {'sport': sport, 'sports': sports, 'games': games})
    
class RegistrationFormView(View):
    form_class = RegistrationForm
    template_name = 'application/landing.html'
    
    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
        
    # process form data
    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            
            user = form.save(commit=False)
            
            # cleaned (normalized) data
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return redirect('/gamelist/')
        
    
    
            
                    
    
    