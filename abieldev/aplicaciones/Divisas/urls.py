from django.urls import path, include
from .views import MoneyPageView

urlpatterns = [
	path('', MoneyPageView.as_view(), name='money'),	
]