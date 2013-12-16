from payment.service_client.PaymentServiceClient import PaymentServiceClient


class PaymentAPI(object):

    def __init__(self):
        self.paymentServiceClient = PaymentServiceClient()