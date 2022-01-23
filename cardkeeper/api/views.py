from rest_framework import generics
from api.models import Team, Player, Card
from api.serializers import CardSerializer, PlayerSerializer, TeamSerializer
from django.shortcuts import get_object_or_404

class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class CardList(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    
    filterset_fields = ['has_auto', 'has_memorbilia', 'in_collection', 'is_watchlisted']

class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    
    filterset_fields = ['first_name', 'team', 'last_name']

class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    
    filterset_fields = ['league', 'name']
   
class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
