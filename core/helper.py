import md5
import base64
from cStringIO import StringIO

def convert2md5(input):
	m1 = md5.new()
	m1.update(input)
	return m1.hexdigest()
def generate_ss_string(server, server_port, password, method):
	ss_string_body = '%s:%s@%s:%s' % (method, password, server, server_port)
	
	ss_string = 'ss://' + base64.b64encode(ss_string_body)
	return ss_string

