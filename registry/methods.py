import json
import xmlrpclib

from django.core.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render_to_response

from xmlrpc.decorators import xmlrpc_func


class PingClient():

    def ping(self, location):
        try:
            rpc_srv = xmlrpclib.ServerProxy(location)
            answer = rpc_srv.ping("PING")
            return answer == "PING"
        except Exception as cre:
            return False


class Services():

    def __init__(self):
        self.services = {}
        self.min_port = 8001
        self.max_port = 8099
        self.used_ports = {}

    def _get_port(self):
        for i in range(self.min_port, self.max_port):
            if i not in self.used_ports:
                self.used_ports[i] = 1
                return i

    def add(self, name):
        port = self._get_port()

        assert port in self.used_ports, 'Port is not in used ports!'
        assert name not in self.services, 'Name is already in services list!'

        self.services[name] = {"location": "http://localhost:%i/xmlrpc/" % port, "port": port}

        assert name in self.services, 'Name should be in services list!'

        return port

    def remove(self, name):
        assert name in self.services

        port = self.services[name]["port"]

        assert port in self.used_ports

        del self.used_ports[port]
        del self.services[name]

        assert port not in self.used_ports
        assert name not in self.services

        return True

    def get_all(self):
        return self.services

    def check(self):
        """ This method checks all services if they are still reachable """
        ping_client = PingClient()
        for key in self.services:
            element = self.services[key]
            if not ping_client.ping(element["location"]):
                self.remove(key)

    def get_status(self, name):
        if name not in self.services:
            return {"status": "red"}
        else:
            ping_client = PingClient()
            success = ping_client.ping(self.services[name]["location"])
            if success:
                return {"status": "green"}
            else:
                return {"status": "yellow"}

    def discover(self, name):
        for key in self.services:
            if name in key:
                return self.services[key]["location"]


services = Services()

@xmlrpc_func(context="registry", returns='integer', args=['string'])
def register(name):
    """Simply returns the args passed to it as a string"""
    return services.add(name)

@xmlrpc_func(context="registry", returns='boolean', args=['string'])
def remove(name):
    """Simply returns the args passed to it as a string"""
    return services.remove(name)

@xmlrpc_func(context="registry", returns='string', args=['string'])
def discover(name):
    """ Discovers a Service by Name"""
    return services.discover(name)

def view_services(request):
    services.check()
    return render_to_response("registry_overview.pyhtml", {"services": services.get_all()})


SERVICES_THAT_SHOULD_BE_AVAILABLE = ["payment1", "location1"]

def get_healthcheck_page(request):
    c = {}
    c.update(csrf(request))
    c["services"] = SERVICES_THAT_SHOULD_BE_AVAILABLE
    return render_to_response("health_check.pyhtml", c)


def check_health(request):
    status = {name: services.get_status(name) for name in SERVICES_THAT_SHOULD_BE_AVAILABLE}
    return HttpResponse(json.dumps(status), mimetype="application/json")
