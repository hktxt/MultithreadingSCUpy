#coding = utf-8
import time
start =time.clock()

f=open("F:\dict.txt",'w+')
chars=['0','1','2','3','4','5','6','7','8','9']
base=len(chars)
end=len(chars)**6
for i in range(0,end):
    n=i
    ch0=chars[n%base]
    n=n/base
    ch1=chars[n%base]
    n=n/base
    ch2=chars[n%base]
    n=n/base
    ch3=chars[n%base]
    n=n/base
    ch4=chars[n%base]
    n=n/base
    ch5=chars[n%base]
    print i,ch5,ch4,ch3,ch2,ch1,ch0
    f.write(ch5+ch4+ch3+ch2+ch1+ch0 + '\n')
f.close()
end = time.clock()
print('Running time: %s Seconds'%(end-start))