import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from api.models import Player, Team, Card

class PlayerAPITestCase(APITestCase):
    """
    Tests pertaining to API methods related to `Player`
    Args:
        APITestCase ([type]): [description]
    """
    
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        
        cls.client = APIClient
        cls.player_url = reverse('players_api')
        cls.team_url = reverse('teams_api')
        cls.card_url = reverse('cards_api')
    
    def test_if_card_exists_do_not_add(self):
        """
        If the card exists, do not add to the database
        """
        
        self._post_test_team()
        self._post_test_player()
        response = self._post_test_card()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Card.objects.count(), 1)
        
        response = self._post_test_card()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Card.objects.count(), 1)
        
    def test_if_player_exists_do_not_add(self):
        """
        If a player exists, do not add to the database
        """
        
        self._post_test_team()
        response = self._post_test_player()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Player.objects.count(), 1)
        
        response = self._post_test_player()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Player.objects.count(), 1)
    
    def test_player_filter_args(self):
        """
        Test filter_args are being respected
        """
        
        self._post_test_team()
        self._post_test_player()

        qs = "team=1"
        req = '?'.join((self.player_url, qs))
        
        response = self.client.get(req)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(response.content)), 1)
        

    def test_team_filter_args(self):
        """
        Test filter_args are being respected
        """
        
        test_data = {
            'name': 'Remu Suzumori',
            'abbreviation': 'ABP',
            'league': 'MLB'
        }
        
        self._post_test_team()
        self._post_test_team(test_data)
        
        qs = 'league=MLB'
        req = '?'.join((self.team_url, qs))
        
        response = self.client.get(req)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(response.content)), 1)
        
    def test_if_exists_do_not_add_team(self):
        """
        Test to ensure duplicate team is not added to the database
        """
        
        response = self._post_test_team()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 1)
        
        response = self._post_test_team()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Team.objects.count(), 1)


    def _post_test_card(self):
        test_data = {
            'player': 1,
            'set': 'Upper Deck',
            'title': '2018/19 Series 1 Young Guns',
            'has_auto': True,
            'has_memorbilia': False,
            'in_collection': True,
            'is_watchlisted': True
        }
        
        return self.client.post(self.card_url, test_data, format='json')
    
    def _post_test_team(self, team=None):
        
        if team is None:
            test_data = {
                'name': 'Sana Minatozaki',
                'abbreviation': 'SANA',
                'league': 'NHL',
            }
        else:
            test_data = team
        
        return self.client.post(self.team_url, test_data, format='json')
        
    def _post_test_player(self):
        test_data = {
            'first_name': 'Trevor',
            'last_name' : 'Linden',
            'team' : 1,
        }
        
        return self.client.post(self.player_url, test_data, format='json')