django_soa_template
===================

This is a template django project with integrated RPC SOA Architecture as well as health check and registry.
There is furthermore a frontend project which makes usage of the ServiceClients which call the services.

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

Now Start the Frontend:

* startFrontend.py

You can now access localhost:8000/test and should see that the PaymentService was called via the PaymentServiceClient

Some notes for development
--------------------------

* Check the __init__.py files of the payment/location/xmlrpc app - they show how to register xmlrpc methods
* Check the startPayment.py as an example of how to register a service at the registry
* Each settings.py is using a different urls.py so be aware of that
* The settings.py in the dedicated application folders are for starting that application and if neccessary the
    xmlrpc-app only
