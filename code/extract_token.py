def extract():
 f = open("out",'r')
 data = f.read()
 data = data.replace('{','')
 data = data.replace('}','')
 data = data.replace('"','')
 data = data.replace(' ','')
 info = data.split(',')
 auth_token = ''
 for element in info:
	wrd = element.split(':')
	if wrd[0]=="id":
		auth_token = wrd[1]
		break
 if auth_token=='':
	return None
 else:
	return auth_token
