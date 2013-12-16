import xmlrpclib
from registry.client.RegistryClient import RegistryClient


class ServiceClient():

    def __init__(self, context):
        self.context = context
        self.registryClient = RegistryClient()
        self.find_service()

    def find_service(self):
        """ This discovers the services for the service client"""
        self.service = self.registryClient.discover_service(self.context)
        self.rpc_srv = xmlrpclib.ServerProxy(self.service)

