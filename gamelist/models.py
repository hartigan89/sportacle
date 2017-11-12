from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse

PICK_CHOICES = (
        ('U', 'Unknown'),
        ('V', 'Visitor'),
        ('H', 'Home'),
        ('T', 'Tie')
    )

# Create your models here.
class Sport(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'sport'
        verbose_name_plural = 'sports'
    
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('game_list_by_sport', args=[self.slug])
    
class Game(models.Model):
    sport = models.ForeignKey(Sport, related_name='games')
    gameTime = models.DateTimeField()
    visitor = models.CharField(max_length=200, db_index=True)
    visitorOdds = models.DecimalField(max_digits=10, decimal_places=2)
    home = models.CharField(max_length=200, db_index=True)
    homeOdds = models.DecimalField(max_digits=10, decimal_places=2)
    outcome = models.CharField(max_length=1, choices=PICK_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
        
    class Meta:
        ordering = ('sport','-updated',)
   
        
 