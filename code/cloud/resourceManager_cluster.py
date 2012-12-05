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
cluster_info = {}
cluster_metrics = {}
node_info = {}

def check_none(inputstr):
	output = re.sub('false','False',inputstr)
	output = re.sub('true','True',inputstr)
	output = re.sub('null','None',inputstr)
	return output

def clusterInfo():
	buf = cStringIO.StringIO()
	c = pycurl.Curl()
	rm_address = configure.rm_address + '/' + 'info'
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
	#to get basic cluster info
	output_dic1 = output_dic['clusterInfo']
	cluster_info[output_dic1['id']] = output_dic1
	print cluster_info
	metricsInfo(output_dic1['id'])	#passing with cluster id to metric parser
	nodeInfo(output_dic1['id'])
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
#	print output_dic
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
#	print output_dic
	#to get basic nodeinfo
	output_dic1 = output_dic['nodes']
	if 'node' in output_dic:
		#all nodes in format cluster_id:[{nodeinfo1},{nodeinfo2}..]
		node_info[cluster_id] = output_dic1['node']
	else:
		node_info[cluster_id] = {}

def main():
	clusterInfo()
	pass

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
