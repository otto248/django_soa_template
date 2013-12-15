from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testrpc.views.home', name='home'),
    # url(r'^testrpc/', include('testrpc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^xmlrpc/$', 'xmlrpc.views.handle_xmlrpc', name='xmlrpc'),

    # The View url for the services
    url(r'^registry/$', 'registry.methods.view_services'),
    url(r'^health/$', 'registry.methods.get_healthcheck_page'),
    url(r'^ajax/check_health/', 'registry.methods.check_health'),

)
