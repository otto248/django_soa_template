import xmlrpclib


class RegistryClient():

    def __init__(self):
        self.rpc_srv = xmlrpclib.ServerProxy("http://localhost:5555/xmlrpc/")

    def register(self, name):
        # Call the Registry to register myself there
        location = self.rpc_srv.register(name)
        assert location is not None

        return location

    def discover_service(self, context):
        assert context is not None
        result = self.rpc_srv.discover(context)
        assert result is not None

        return result