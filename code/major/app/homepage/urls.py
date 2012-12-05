from django.conf.urls.defaults import *
from django.contrib.auth.views import login,logout
urlpatterns=patterns('',
	(r"^$",'major.app.homepage.views.index'),
	)
urlpatterns=patterns('',
	url(r'^login/$','auth.views.login_user',{'template_name':'auth1.html'}),
	)
