from django.shortcuts import render
from django.views.generic.base import TemplateView
from .apis.api_localbit import precio_dolar, btc_in_bs, btc_in_usd
# Create your views here.

global precio_dolar
global btc_in_bs
global btc_in_usd


class MoneyPageView(TemplateView):
    template_name = "Divisas/money.html" 

    def get(self, request, *args, **kwargs):
    	context = locals()
    	context['precio_dolar'] = round(float(precio_dolar))
    	context['btc_in_bs'] = round(float(btc_in_bs))
    	context['btc_in_usd'] = round(float(btc_in_usd))
    	return render(request, self.template_name, context)
