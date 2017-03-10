from django.views.generic.base import View
from django.http import JsonResponse

class PlayView(View):
    def dispatch(request, *args, **kwargs):
        print(request)
        return JsonResponse({'body': { 'accountBalance': '1000'} })
