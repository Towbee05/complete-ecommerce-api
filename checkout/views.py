from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import stripe
from decouple import config

# Create your views here.
class CheckoutView(APIView):
    def get(self, request):
        charge = stripe.Charge.retrieve(
            "ch_3Ln3e92eZvKYlo2C0eUfv7bi",
            api_key=config("STRIPE_API_KEY")
        )
        charge.capture()
        print(charge)
        return Response({
            'detail' : 'GET request on the checkout view'
        })
    
    def post(self, request):
        return Response({
            'detail' : 'POST request on the checkout view'
        })