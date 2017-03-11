from django.views.generic.base import View
from django.http import JsonResponse
import json

class PlayView(View):
    def dispatch(self, *args, **kwargs):
        json_data = json.loads(self.request.body.decode('utf-8'))
        profile = self.request.user.profile
        return JsonResponse({'body': {
            'accountBalance': profile.account_balance + 10 * json_data['level'] + json_data['guess'],
            'currentLevel' : 4,
            'result' : {
                0: {0: 'W', 1: 'L'},
                1: {0: 'W', 1: 'L'},
                2: {0: 'W', 1: 'L'},
                3: {0: 'W', 1: 'L'},
                4: {0: 'W', 1: 'L'},
                5: {0: 'W', 1: 'L'},
                6: {0: 'W', 1: 'L'},
            }
        } })
