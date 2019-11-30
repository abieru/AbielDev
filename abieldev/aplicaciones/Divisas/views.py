from django.shortcuts import render
from django.views.generic.base import TemplateView
from .apis.api_localbit import *
# Create your views here.



class MoneyPageView(TemplateView):
    template_name = "Divisas/money.html" 

    def get(self, request, *args, **kwargs):
    	context = locals()
    	context['usd_in_ves'] = Dolartoday()
    	context['btc_in_bs'] = BtcInVes()
    	context['btc_in_usd'] = BtcInUsd()
    	return render(request, self.template_name, context)

