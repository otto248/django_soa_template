import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:8001/xmlrpc')
location = s.ping("standalone")
print location