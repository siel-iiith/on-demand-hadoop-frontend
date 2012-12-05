from django.conf.urls import patterns, include, url

from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^$','auth.views.login_user'),
	(r'^login/$','auth.views.login_user'),
    (r'^userhome','major.app.views.userhome'),
    (r'^xml','major.app.views.xml'),
    (r'^adminhome(?P<path>/.*)','major.app.views.adminhome'),

    (r'^logout/$','logout_page'),
    (r'^editjob','major.app.views.editjob'),
    (r'^extract/$','major.app.views.extract'),
    (r'^filebrowser(?P<path>/.*)','major.app.views.filebrowser'),
    (r'^filebrowsero(?P<path>/.*)','major.app.views.filebrowsero'),
    (r'^logs(?P<path>/.*)','major.app.views.logs'),
    (r'^userjob(?P<path>/.*)','major.app.views.userjob'),
    


    # Examples:
    # url(r'^$', 'major.views.home', name='home'),
    # url(r'^major/', include('major.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
