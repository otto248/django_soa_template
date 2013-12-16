from share.ServiceClient import ServiceClient


class PaymentServiceClient(ServiceClient):

    def __init__(self):
        # Define the Context of this service client
        # This also discovers the service and binds it to a variable
        ServiceClient.__init__(self, 'payment')


    def make_payment(self, param):
        return self.rpc_srv.make_payment(param)





