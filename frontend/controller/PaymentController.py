from django.core.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import View


class PaymentController(View):

    # Define the APIs used
    paymentAPI = None

    def __init__(self, paymentAPI):
        self.paymentAPI = paymentAPI

    def get(self, request):


        c = {"result" : self.paymentAPI.paymentServiceClient.make_payment("Test")}
        c.update(csrf(request))

        return render_to_response("payment.pyhtml", c)

    def post(self, request):
        response = HttpResponse("You made a post")
        return response