from rest_framework import serializers
from .models import Log, Wallet

class LogSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=180)
    completed = serializers.BooleanField()


    class Meta:
        model = Log
        fields = ('__all__')

class WalletSerializer(serializers.ModelSerializer):

    total = serializers.IntegerField()
    amount    = serializers.IntegerField()
    user_id = serializers.IntegerField()
    transactiontype = serializers.CharField()
    transactiondate = serializers.DateTimeField()
    reference_id = serializers.CharField()
    class Meta:
        model = Wallet
        fields = ('__all__')
