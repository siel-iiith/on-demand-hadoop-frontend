import string
import os

def replace_char(command):
	my_list=[]
	for ch in command:
		my_list.append(ch)
	for i in range(len(my_list)):
		if my_list[i] == "#":
			my_list[i] = "'"
		elif my_list[i] == "@":
			my_list[i] = '"'
	command = ''.join(my_list)
	return command

def curl_auth(usr,ps):

	command = 'curl -s -H #Content-type: application/json# -d #{@auth@: {@passwordCredentials@: {@username@: @'
	command+=usr
	command+='@, @password@: @'
	command+=ps
	command+='@}}}# --noproxy 10.2.4.129 http://10.2.4.129:5000/v2.0/tokens'
	command = replace_char(command)
        os.system(command)
if __name__=='__main__':
    import sys
    usr=sys.argv[1]
    ps=sys.argv[2]
    curl_auth(usr,ps)


