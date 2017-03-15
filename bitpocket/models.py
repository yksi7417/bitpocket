from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import json

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_balance = models.IntegerField(default=0)
    current_level = models.IntegerField(default=0)
    num_of_games_played = models.IntegerField(default=0)
    game_result = models.TextField(blank=True)
    bet_size = models.IntegerField(default=0)
    pot = models.IntegerField(default=0)
    cost = models.IntegerField(default=2)
    message = models.TextField(blank=True)

    def collect_wager(self):
        self.account_balance += self.pot
        self.reset_game_result()

    def start_game(self):
        if (self.account_balance > self.bet_size):
            self.bet_size = 100
            self.reset_game_result()
            self.account_balance -= self.bet_size
            self.pot = self.bet_size
            self.message = "play!"
        else:
            self.pot = 0
            self.message = "insufficient account balance, please recharge"
            self.current_level = -1


    def win_game(self):
        self.pot = self.pot * 2 - self.cost

    def loss_game(self):
        self.pot = 0

    def reset_game_result(self):
        self.game_result = ''
        self.current_level = 0

    def append_line_result(self, line_number, line_result):
        if (self.game_result != ''):
            game_result_dict = json.loads(self.game_result)
        else:
            game_result_dict = {}
        game_result_dict[str(line_number)] = {}
        game_result_dict[str(line_number)]['0'] = line_result[0]
        game_result_dict[str(line_number)]['1'] = line_result[1]
        self.game_result = json.dumps(game_result_dict)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
