from django.db import models

class Team(models.Model):
    """
    represents a team in a sports league

    Args:
        models ([type]): [description]
    """
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=5, default='')
    league = models.CharField(max_length=3)
    
    class Meta:
        unique_together = ('name', 'league')
        ordering = ['created']
        
class Player(models.Model):
    """
    represents a player on a team

    Args:
        models ([type]): [description]
    """
    
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="players")
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_watchlisted = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('first_name', 'last_name', 'team')
        ordering = ['created']

class Card(models.Model):
    """
    represents a card in a collection

    Args:
        models ([type]): [description]
    """
    
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="cards")
    created = models.DateTimeField(auto_now_add=True)
    set = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    has_auto = models.BooleanField(default=False)
    has_memorbilia = models.BooleanField(default=False)
    in_collection = models.BooleanField(default=False)
    is_watchlisted = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('title', 'player')
        ordering = ['created']
        