#Resource Server Address to be obtained

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
apps_info = {}
app_vs_user = {}
empty = {}

def check_none(inputstr):
	output = re.sub('false','False',inputstr)
	output = re.sub('true','True',inputstr)
	output = re.sub('null','None',inputstr)
	return output

def app_vs_userfunc(username):
	if username in app_vs_user:
		return app_vs_user[username]
	else:
		return empty

def appsInfo():
	buf = cStringIO.StringIO()
	c = pycurl.Curl()
	rm_address = configure.rm_address + '/' + 'apps'
	print "Connecting to", rm_address
	c.setopt(c.URL,rm_address)

	rm_proxy = configure.rm_address +':'+ configure.rm_port

	c.setopt(pycurl.PROXY,rm_address)
	c.setopt(c.WRITEFUNCTION, buf.write)
	c.perform()
	output = buf.getvalue()
#	print output		#the entire output
	output = json.dumps(output)	
	output_dic = json.loads(output)
	output_dic = check_none(output_dic)
	output_dic = ast.literal_eval(output_dic)
#	print output_dic
	#to get basic app info
	output_dic1 = output_dic['apps']
#	print output_dic1
	if output_dic1 is None:
		pass
	elif 'app' in output_dic1:
		for value in output_dic1['app']:
			apps_info[value['id']] = value		# maps application id to a dictionary of values
			app_vs_user[value['user']] = value
	
	print "ooooooooo"
	print apps_info

	
	buf.close()

def metricsInfo(cluster_id):
	buf = cStringIO.StringIO()
	c = pycurl.Curl()
	rm_address = configure.rm_address + '/' + 'metrics'
	print "Connecting to", rm_address
	c.setopt(c.URL,rm_address)

	rm_proxy = configure.rm_address +':'+ configure.rm_port

	c.setopt(pycurl.PROXY,rm_address)
	c.setopt(c.WRITEFUNCTION, buf.write)
	c.perform()
	output = buf.getvalue()
#	print output		#the entire output
	output = json.dumps(output)	
	output_dic = json.loads(output)
	output_dic = check_none(output_dic)
	
	output_dic = ast.literal_eval(output_dic)
	print output_dic
	#to get basic cluster info
	output_dic1 = output_dic['clusterMetrics']
	cluster_metrics[cluster_id] = output_dic1
	print cluster_metrics

def nodeInfo(cluster_id):
	buf = cStringIO.StringIO()
	c = pycurl.Curl()
	rm_address = configure.rm_address + '/' + 'nodes'
	print "Connecting to", rm_address
	c.setopt(c.URL,rm_address)

	rm_proxy = configure.rm_address +':'+ configure.rm_port

	c.setopt(pycurl.PROXY,rm_address)
	c.setopt(c.WRITEFUNCTION, buf.write)
	c.perform()
	output = buf.getvalue()
#	print output		#the entire output

	output = json.dumps(output)	
	output_dic = json.loads(output)
	output_dic = check_none(output_dic)
	output_dic = ast.literal_eval(output_dic)
	print output_dic
	#to get basic nodeinfo
	output_dic1 = output_dic['nodes']
	print output_dic1
	if 'node' in output_dic:
		#all nodes in format cluster_id:[{nodeinfo1},{nodeinfo2}..]
		node_info[cluster_id] = output_dic1['node']
	else:
		node_info[cluster_id] = {}

def main():
	appsInfo()
	pass

if __name__ == '__main__':
	main()
