from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from frontend.controller.PaymentController import PaymentController
from payment.api.PaymentAPI import PaymentAPI



# Create the controller used for the mapping
payment_controller = PaymentController.as_view(paymentAPI=PaymentAPI())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testrpc.views.home', name='home'),
    # url(r'^testrpc/', include('testrpc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^payment/', payment_controller)
)