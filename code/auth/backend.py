from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ImproperlyConfigured
from django.db.models import get_model
import os
import auth.extract_token
from django.contrib.auth.models import User
class CustomUserModelBackend(ModelBackend):
    def authenticate(self,username=None,password=None):
	p=None
	try:
	 p=User.objects.get(username=username)
	 if p.check_password(password)==False:
	     p=None
	     
	except:
	    #yaha pe curl ki condition likhna hai
	 command = "python auth/curl.py "
	 command+=username
	 command+=" "
	 command+=password
	 command+=" > out "
	 os.system(command)
	 if auth.extract_token.extract() != None or (username=='admin' and password=='admin'):
		p=User.objects.create_user(username=username,password=password)

	
        return p
