#History Server Address to be obtained

import pycurl
import cStringIO
import sys
import urllib
import json
import re
import unicodedata
import configure
import ast

output_dic = {}
specific_job_details = {}
history_vs_user = {}

def get_jobinfo(output_dic):
#	print output_dic
#	for i in output_dic:
#		print i,output_dic[i]
	job_list = output_dic['jobs']
	for key in job_list:
		specific_job_details[job_list[key][0]['id']] = job_list[key][0]
		history_vs_user[job_list[key][0]['user']] = job_list[key][0]
	print specific_job_details

def main():
	buf = cStringIO.StringIO()
	c = pycurl.Curl()
	hs_address = configure.hs_address
	print "Connecting to", hs_address
	c.setopt(c.URL,hs_address)

	hs_proxy = configure.hs_address +':'+ configure.hs_port

	c.setopt(pycurl.PROXY,hs_address)
	c.setopt(c.WRITEFUNCTION, buf.write)
	c.perform()
	output = buf.getvalue()
#	print output		#the entire output
	output = json.dumps(output)	
	output_dic = json.loads(output)
	output_dic = ast.literal_eval(output_dic)
#	print output_dic
	#to get list of history jobs
	get_jobinfo(output_dic)
	

	buf.close()

if __name__ == '__main__':
	main()
"""
tryjsn=json.loads(output)
filelist=[]
tryjsn=tryjsn['FileStatuses']
tryjsn=tryjsn['FileStatus']
for i in tryjsn:
    y=[]
    for j in i:
      if j=='pathSuffix' or j=='type':
	 p=unicodedata.normalize('NFKD',i[j]).encode('ascii','ignore')
         y.append(p)
    filelist.append(y)
print filelist
"""
