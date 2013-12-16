from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:5555/xmlrpc/')
location = s.register("standalone")


from SimpleXMLRPCServer import SimpleXMLRPCServer as Server

class Handler(SimpleXMLRPCRequestHandler):

    rpc_paths = ('/xmlrpc/')

def fak(n):
    """ Berechnet die Fakultaet der ganzen Zahl n. """
    erg = 1
    for i in xrange(2, n+1):
        erg *= i
    return erg

def quad(n):
    """ Berechnet das Quadrat der Zahl n. """
    return n*n

def ping(msg):
    """Simply returns the args passed to it as a string"""
    return str(msg)

srv = Server(("localhost", location), requestHandler=Handler)
srv.register_introspection_functions()
srv.register_function(fak)
srv.register_function(quad)
srv.register_function(ping)
srv.serve_forever()