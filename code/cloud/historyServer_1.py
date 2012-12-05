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
import re

output_dic = {}
more_job_details = {}

def get_jobinfo(output_dic):
	print output_dic
#	for i in output_dic:
#		print i,output_dic[i]
	#key is job id and value is a dictionary of details..
	more_job_details[output_dic['job']['id']] = output_dic['job']
	print more_job_details

def main_func(job_id):
	buf = cStringIO.StringIO()
	c = pycurl.Curl()
	hs_address = configure.hs_address+'/'+str(job_id)
	print "Connecting to", hs_address
	c.setopt(c.URL,hs_address)

	hs_proxy = configure.ip_address +':'+ configure.hs_port
	print "Connecting to", hs_proxy

	c.setopt(pycurl.PROXY,hs_proxy)
	c.setopt(c.WRITEFUNCTION, buf.write)
	c.perform()
	output = buf.getvalue()
	print output		#the entire output
	output = json.dumps(output)	
	output_dic = json.loads(output)
	output_dic = re.sub('false','False',output_dic)
	output_dic = re.sub('true','True',output_dic)
	output_dic = ast.literal_eval(output_dic)
#	print output_dic
	#to get list of history jobs
	get_jobinfo(output_dic)
	

	buf.close()
def main():
	main_func('job_1352454713396_0001')
	pass
if __name__ == '__main__':
	main()
