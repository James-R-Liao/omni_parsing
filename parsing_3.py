__author__ = 'james_liao'

import re

filein = open(r'D:\Personal_Study\Work_By_Myself\test_read_Rx_Abnomral_9.txt','rb')
#p = r'((20 20 20 20 20)+\r\n70)'#\n70 6B 74 73
#p = r'(20 20 20 20 20 \r\n70 6B 74 73){1}[0-9A-Z\40\r\n]?#'
#p = re.compile(p)
pattern = '20 20 20 20 20 \r\n70 6B 74 73'
data = filein.read()
pat_idx = data.find(pattern)
frt_pkt_idx = pat_idx + 47

print pat_idx
print data[pat_idx:pat_idx+47] #start of first packet
print data[frt_pkt_idx:frt_pkt_idx+128]

Pure_dat = data.replace(r'[\r\n\40]','')

print 



