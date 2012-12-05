#!/bin/python
import config_hadoop
import os
import subprocess
import string

def run(jar,job, input_dir, output_dir):
    cmd1 = ' script -c \''+ config_hadoop.hadoop_system+"/bin/hadoop "+ 'jar '+ jar + ' ' + job + ' ' + input_dir + ' ' + output_dir +'test_output\'  site_logs'
    print cmd1
    cmd2 = ' bash '+config_hadoop.hadoop_system+'/start_yarn.sh'
    print cmd2
    cmdf1 = 'ssh '+config_hadoop.username+'@'+config_hadoop.namenode_ip+cmd1
    cmdf2 = 'ssh '+config_hadoop.username+'@'+config_hadoop.namenode_ip+cmd2
    print cmdf2
    try:
	job = os.system(cmd2)
	job = os.system(cmd1)
        new_output_dir(output_dir)
    except:
	print "hello"
    print job	
    pass
def new_output_dir(orig_dir):
    #following two lines can be commented if single cluster
#    cmdcp = 'scp '+config_hadoop.username+'@'+config_hadoop.namenode_ip+':'+config_hadoop.hadoop_system+'/site_logs'+' ./'
#    job2 = os.system(cmdcp)
    f = open('site_logs')
    for lines in f:
	listf = lines.split()
	if 'application' in listf and 'Submitted' in listf:
	    new = listf[6]
	    break
    f.close()
    new_dir = new.replace('application','output')
    print "new",new_dir
    cmdrcp =  config_hadoop.hadoop_system+"/bin/hadoop dfs -cp "+orig_dir+"test_output "+new_dir      
    cmdrep =  config_hadoop.hadoop_system+"/bin/hadoop dfs -rm -r "+orig_dir+"test_output"
    os.system(cmdrcp)
    os.system(cmdrep)
    print 'done!'

    pass
def main():
    jar = config_hadoop.hadoop_system+'/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.0.2-alpha.jar'
    job = 'wordcount'
    input_dir = 'input'
    output_dir = 'test_output'
    
    run(jar,job,input_dir,output_dir)
    new_output_dir()
    pass

if __name__ == '__main__':
    main()
