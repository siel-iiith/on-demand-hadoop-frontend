from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	    (r'^login/$', 'auth.views.login_user'),
	    
	    )
urlpatterns = patterns('',
	        (r'^filebrowser(?P<path>/.*)','major.app.views.filebrowser'),
		)
urlpatterns=patterns('',
	    (r'^userhome','major.app.views.userhome'),
	    (r'^adminhome(?P<path>/.*)','major.app.views.adminhome'),
	    )+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

