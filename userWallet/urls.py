from django.urls import path
from .views import (LogViews, GetWallet, AddMoney, GetDailyTransactions)

urlpatterns = [
    path('logs', LogViews.as_view()),
    path('get-balance/<int:userId>', GetWallet.as_view(), name='get-balance'),
    path('add-money/<int:userId>', AddMoney.as_view(), name='add-money'),
    path('daily-transactions', GetDailyTransactions.as_view(), name='daily-transactions'),
]
