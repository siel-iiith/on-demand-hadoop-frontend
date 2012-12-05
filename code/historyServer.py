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

def get_jobinfo(usr_name):
#	history_vs_user = {}
#	print output_dic
#	for i in output_dic:
#		print i,output_dic[i]
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
	print output_dic
	if 'null' not in output_dic:
		output_dic = ast.literal_eval(output_dic)
	#to get list of history jobs
		job_list = output_dic['jobs']
		print job_list
		if 'job' in job_list:
			job_list1 = job_list['job']
#			print job_list1
			for key in job_list1:
				print "KEY",key
				specific_job_details[key['id']] = key
				k = key['user']
#				print k
				if k in history_vs_user:
					history_vs_user[k].append(key)
				else:
					history_vs_user[k] = []
					history_vs_user[k].append(key)

#		print '  job details:  ',specific_job_details
	buf.close()
#	for i in history_vs_user["surya"]:
#		print "check",i
#	print '  user:  ',history_vs_user["surya"]
	print history_vs_user # Each username is a key: value is a (list of)dictionary of job details
	return history_vs_user # Each username is a key: value is a (list of)dictionary of job details
#	print "ifooahfnaoidhfshgiuos",history_vs_user[key][0],usr_name,
#	print history_vs_user[key][0][usr_name]
#	return history_vs_user[key][0][usr_name]

def main():
	pass
	x = get_jobinfo('saumyad')

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
