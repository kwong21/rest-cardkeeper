from rest_framework import serializers
from api.models import Team, Player, Card

class CardSerializer(serializers.HyperlinkedModelSerializer):
    player = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all(), many=False)
    
    class Meta:
        model = Card
        fields = ['id', 'set', 'title', 'has_auto', 'has_memorbilia', 'in_collection', 'is_watchlisted', 'player']
        read_only_fields = ['id', 'player']
        
class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), many=False)
    
    class Meta:
        model = Player
        fields = ['id', 'first_name', 'last_name', 'team', 'is_watchlisted']
        read_only_fields = ['id']
        
class TeamSerializer(serializers.HyperlinkedModelSerializer):
    players = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'abbreviation', 'league', 'players']
        read_only_fields = ['id']
