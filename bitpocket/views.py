from django.views.generic.base import View
from django.http import JsonResponse

class PlayView(View):
    def dispatch(self, *args, **kwargs):
        profile = self.request.user.profile
        return JsonResponse({'body': { 'accountBalance': profile.account_balance } })
