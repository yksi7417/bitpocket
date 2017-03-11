from django.views.generic.base import View
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json

from django.core import serializers

class PlayView(View):
    def dispatch(self, *args, **kwargs):
        json_data = json.loads(self.request.body.decode('utf-8'))
        profile = self.request.user.profile
        dict = { 'body' : model_to_dict(profile) }
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
