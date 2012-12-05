# Create your views here.
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.shortcuts import render
from django.template import RequestContext
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from major.app.models import *
from django.shortcuts import render_to_response
import pycurl
import cStringIO
import sys
import json
import os.path, time
from os.path import join, getsize
import urllib
import unicodedata
from django.contrib.auth.decorators import login_required
import historyServer as hs
import historyServer_1 as job_h
import resourceManager_app as ra
usr_name = ''
gu=0
	    
#def user_home(request):
#        return render_to_response('auth.html',{'state':state,'username':username,'password':password},RequestContext(request,{}))
def login_user(request):
    state="please log in below"
    global usr_name
    username=password=''
    if request.POST:
	username=request.POST.get('username')
    usr_name = username
    password=request.POST.get('password')
    user=authenticate(username=username,password=password)
    if user==None:
	    state="your username and password are incorrect"	
            return render_to_response('auth.html',{'state':state,'username':username,'password':password},RequestContext(request,{}))
    else:
        return redirect("http://127.0.0.1/userhome/")
		    
        return render_to_response('auth.html',{'state':state,'username':username,'password':password},RequestContext(request,{}))


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

def logs(request,path):
  path=unicodedata.normalize('NFKD',path).encode('ascii','ignore')
  Hadoop_log='/home/surya/yarn/hadoop/logs'
  j=0
  lines=[]
  links=[]
  print Hadoop_log+path
  if len(path)>1:
        g=1
	print "here"
	filelist=[]
	f=open(Hadoop_log+path,'r')
	print f
	try:
	 lines=f.readlines()
	 #print lines
	 lines=map(lambda s:s.strip(),lines)
	 #print lines
	except:
	    j=1
  else:
     g=0
     for root, dirs, files in os.walk(Hadoop_log):
        for file in list(files):

         fileaddress = os.path.join(root, file)
         tmp=file
	 o=[]
	 o.append(file)
   #     print(file)
         h=time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(os.path.getmtime(fileaddress)))
         tmp=tmp+' '+h
         tmp=tmp+' '+str(os.path.getsize(fileaddress))
         o.append(tmp)
	 lines.append(o)
  print lines
  length=range(len(lines))
  return render_to_response('logs.html',{'length':length,'g':g,'lines':lines,'links':links},RequestContext(request,{}))

#@login_required
def filebrowser(request,path):
  print path
  print "i m here"
  buf = cStringIO.StringIO()
  c = pycurl.Curl()
  u='http://localhost:50070/webhdfs/v1'
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
  c.setopt(pycurl.PROXY,'localhost:50070')
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
  global gu
  if gu==0:
      name='filebrowser.html'
  else:
      name='myfile.html'

  print name
  return render_to_response(name,{'filelist':filelist,'path':path,'g':g,})
#login_required()
def filebrowsero(request,path):
    global gu
    gu=1
    h=filebrowser(request,path)
    return h

def userhome(request):
    inst=Job()
    if request.method=='POST':
	jform=JobForm(request.POST,request.FILES,instance=inst)
	if jform.is_valid():
	    jarfile=Job(jar_file=request.FILES['jar_file'])
	    jar_loc=inst.jar_file
	    data=jform.cleaned_data
	    name=data['name']
	    input_path=data['input_path']
	    output_path=data['output_path']
	    print name,input_path,output_path,jar_loc
	    jform.save()
    else: 
	jform=JobForm()
    return render(request,'blah.html',{'jform': jform,})

def userjob(request,path):
	global usr_name
	g=3
	app=0
	if len(path)>1:
	    g=1
#	    print "ooooooooooooo",path.split('_')[0]
	    if path.split('_')[0] == "/application":
			ra.appsInfo()
			path=path.split('/')
			path=path[-1]
			print "\n\ncheck\n\n",ra.apps_info[path],'\n'
			app=1
			dic_apps = ra.apps_info[path]
	    else:
			path=path.split('/')
			path=path[-1]    
	    print ":::::::::::::::::path:::::::::",path
#    job_h.main_func(path)
#	    more_info = job_h.more_job_details
#	    print more_info
	else:
	 g=0
	usr_name = 'surya'   #just for testing
	path=unicodedata.normalize('NFKD',path).encode('ascii','ignore')
	ra.appsInfo()
	print "   inside views    "
	dic_running = ra.app_vs_userfunc("saumyad")
	print "########running list",dic_running
	
	dic_finished = hs.get_jobinfo(usr_name)
	if usr_name in dic_finished:
		print dic_finished[usr_name]
	print dic_running
#	print path

	return render(request,'userjob.html',{'app':app,'g':g,'dic_running':dic_running,'dic_finished':dic_finished[usr_name],'path':path})

def adminhome(request):

	return render(request,'adminhome.html')
