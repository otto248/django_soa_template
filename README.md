django_soa_registry_healthcheck_template
========================================

This is a template django project with integrated RPC SOA Architecture as well as health check and registry.


To use this in action just clone the repository and execute it with django.

First execute:

* startRegistry.py

On http://localhost:5555/xmlrpc/ you should see a list of methods.
On http://localhost:5555/registry you can view registered services.
On http://localhost:5555/health/ you can see a health check monitor.

Now execute:

* startPayment.py

You should see a change on the health check monitor from red to green.
Furthermore on the /registry page the service should be listed.



Some notes for development
--------------------------

* Check the __init__.py files of the payment/location app - they show how to register methods
* Check the settings.py where the methods are registered based on the apps that are turned on
* Check the startPayment.py as an example of how to turn on certain apps with a start script
