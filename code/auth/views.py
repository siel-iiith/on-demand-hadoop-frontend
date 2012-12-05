# Create your views here.
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.shortcuts import render
from django.shortcuts import redirect
from django.template import RequestContext
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from major.app.models import *
from django.shortcuts import render_to_response
import pycurl
import cStringIO
import sys
import json
import urllib
import unicodedata
#def user_home(request):
#        return render_to_response('auth.html',{'state':state,'username':username,'password':password},RequestContext(request,{}))
def login_user(request):
	state="please log in below"
	user=None
	username=password=''
	if request.POST:
		username=request.POST.get('username')
	
		password=request.POST.get('password')
		user=authenticate(username=username,password=password)
#	print username,password
#	print user
		if user==None:
			state="your username and password are incorrect"	
			return render_to_response('auth.html',{'state':state,'username':username,'password':password},RequestContext(request,{}))
		elif username=="admin" and password=="admin":
			return redirect('http://127.0.0.1:8000/adminhome',RequestContext(request,{}))
		else:
			return redirect('http://127.0.0.1:8000/userhome',RequestContext(request,{}))
	else:	    
		return render_to_response('auth.html',{'state':state,'username':username,'password':password},RequestContext(request,{}))


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

def userhome(request):
    inst=Job()
    if request.method=='POST':
	jform=JobForm(request.POST,request.FILES,instance=inst)
	if jform.is_valid():
	    jarfile=Job(jar_file=request.FILES['jar_file'])
	    jform.save()
    else: 
	jform=JobForm()
    return render(request,'userhome.html',{'jform': jform, })

def filebrowser(request,path):
  print path
  buf = cStringIO.StringIO()
  c = pycurl.Curl()
  u='http://10.1.98.101:50070/webhdfs/v1'
  path=unicodedata.normalize('NFKD',path).encode('ascii','ignore')
  print "*********************"
  print path

  if (len(path)>1 and path[1]=='/'):
      path=path.split('/')[2]
      path='/'+path
  
  u=u+path
  print type(path)

  u=u+'?op=LISTSTATUS'
  print u

  parent=path.split('/')
  parent_path=parent[-2]
  g='/'+parent_path
  print "GGGGG"
  print g
  c.setopt(c.URL,u)
  c.setopt(pycurl.PROXY,'10.1.98.101:50070')
  c.setopt(c.WRITEFUNCTION, buf.write)
  c.perform()
  o= buf.getvalue()
#print o
  tryjsn=json.loads(o)
  filelist=[]
  y=0
  try:
   tryjsn=tryjsn['FileStatuses']
  except:
   y=1
  try:
   tryjsn=tryjsn['FileStatus']
  except:
   y=1
  for i in tryjsn:
    y=[]
    for j in i:
      if j=='pathSuffix' or j=='type':
	 p=unicodedata.normalize('NFKD',i[j]).encode('ascii','ignore')
         y.append(p)
    filelist.append(y)
  print filelist 
  #print filelist[0][0]
  buf.close()


  return render_to_response('filebrowser.html',{'filelist':filelist,'path':path,'g':g})

