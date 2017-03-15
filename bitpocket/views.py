from django.views.generic.base import View
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json
import random

from django.core import serializers

class PlayView(View):

    def __flip(self, guess):
        if guess == 0:
            return 1
        return 0

    def __resetGame(self, profile):
        profile.reset_game_result()
        profile.save()

    def __handleWin(self, guess, profile):
        profile.account_balance += 10
        line_result = self.__processLineResult(guess, 'W', 'L')
        profile.append_line_result(profile.current_level, line_result)
        profile.current_level += 1
        profile.save()

    def __processLineResult(self, guess, first, second):
        line_result = ['?', '?']
        line_result[guess] = first
        line_result[self.__flip(guess)] = second
        return line_result

    def __handleLoss(self, guess, profile):
        profile.account_balance -= 10
        line_result = self.__processLineResult(guess, 'L', 'W')
        profile.append_line_result(profile.current_level, line_result)
        profile.current_level += 1
        profile.save()

    def __getResultFromVerifiableSource(self):
        ##  this is not verifiable yet!    mock with random.math for now.
        randomNum = random.choice([0,1])
        if (randomNum < 0.5):
            return 0
        else:
            return 1

    def makeOneGuess(self, profile, guess) :
        result = self.__getResultFromVerifiableSource()
        if (guess == result):
            self.__handleWin(guess, profile)
        else:
            self.__handleLoss(guess, profile)

    def dispatch(self, *args, **kwargs):
        json_data = json.loads(self.request.body.decode('utf-8'))
        profile = self.request.user.profile

        if (json_data['guess'] == -1):
            self.__resetGame(profile)
        else:
            self.makeOneGuess(profile, json_data['guess'])

        dict = { 'body' : model_to_dict(profile) }
        if (dict['body']['game_result'] == ''):
            dict['body']['game_result'] = {}
        else:
            dict['body']['game_result'] = json.loads(dict['body']['game_result'] )

        return JsonResponse(dict)


        # sample result, I want to put this into test case;  how?
        # return JsonResponse({'body': {
        #     'accountBalance': profile.account_balance + 10 * json_data['level'] + json_data['guess'],
        #     'currentLevel' : 4,
        #     'result' : {
        #         0: {0: 'W', 1: 'L'},
        #         1: {0: 'W', 1: 'L'},
        #         2: {0: 'W', 1: 'L'},
        #         3: {0: 'W', 1: 'L'},
        #         4: {0: 'W', 1: 'L'},
        #         5: {0: 'W', 1: 'L'},
        #         6: {0: 'W', 1: 'L'},
        #     }
        # } })
