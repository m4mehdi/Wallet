from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import LogSerializer, WalletSerializer
from .models import Log, Wallet
import time
from datetime import datetime, timedelta

class LogViews(APIView):
    def post(self, request):
        serializer = LogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"status": "success", "response": serializer.data},safe=False, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"status": "error", "response": serializer.errors},safe=False, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, id=None):
        if id:
            item = Log.objects.get(id=id)
            serializer = LogSerializer(item)
            return JsonResponse({"status": "success", "response": serializer.data},safe=False, status=status.HTTP_200_OK)

        items = Log.objects.all()
        serializer = LogSerializer(items, many=True)
        return JsonResponse({"status": "success", "response": serializer.data},safe=False, status=status.HTTP_200_OK)

class GetWallet(APIView):
    def get(self, request, userId):
        if Wallet.objects.filter(user_id = userId).exists():
            response= Wallet.objects.filter(user_id = userId).latest('transactiondate')
            return JsonResponse({"status":"Success", 'total':response.total},safe=False, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"status":"Error", "message":"Wallet for user with this id not found"},safe=False, status=status.HTTP_400_BAD_REQUEST)

class AddMoney(APIView):
    def post(self, request, userId):
        amount = request.data.get('amount', '')
        if isinstance(amount, int):
            if(amount > 0):
                type = 'Refound'
            else:
                type = 'Deduction'
            x = time.time()
            reference_id = str(int(x))
            if Wallet.objects.filter(user_id = userId).exists():
                response= Wallet.objects.filter(user_id = userId).latest('transactiondate')
                total = response.total + amount
            else:
                total = amount

            date = datetime.utcnow()
            serializer = WalletSerializer(data={'total':total,'amount':amount,'user_id':userId,
            'transactiontype':type, 'transactiondate':date, 'reference_id':reference_id})
            if serializer.is_valid():
                serializer.save()
                qrres = 'Success'
                return JsonResponse({"status":qrres, "response":serializer.data},safe=False, status=status.HTTP_200_OK)
            else:
                qrres = serializer.errors
                return JsonResponse({"status":"Error", "response":serializer.errors},safe=False, status=status.HTTP_400_BAD_REQUEST)

        else:
            return JsonResponse({"status":"Error", "message":"Amount of money should be a int"},safe=False, status=status.HTTP_400_BAD_REQUEST)

class GetDailyTransactions(APIView):
    def get(self, request):
        date_from = datetime.now() - timedelta(days=1)
        print('date_from=',date_from)
        response = Wallet.objects.filter(transactiondate__gt = date_from)
        totalTransactions = 0
        for i in range(response.count()):
            totalTransactions = totalTransactions + response[i].amount

        return JsonResponse({"status":"Success", 'total':totalTransactions},safe=False, status=status.HTTP_200_OK)
