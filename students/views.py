from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

def my_first_programe(request):
    return HttpResponse("Hello guys!")

class walletinfoview(APIView):
    def get(self, request):
        wallet_info={
            "name":"Nazmul",
            "Amount": 100,
            "type" : 'usd',
            "exp": "2026",
            "active": True,
        }

        return Response(wallet_info)