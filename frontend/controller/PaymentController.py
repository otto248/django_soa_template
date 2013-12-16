from django.http import HttpResponse
from django.views.generic import ListView, View
from payment.service_client import PaymentServiceClient

__author__ = 'sheepy'


class PaymentController(View):

    def __init__(self):
        self.payment_service_client = PaymentServiceClient()

    def get(self, request):
        response = HttpResponse(self.payment_service_client.make_payment("Test"))
        return response