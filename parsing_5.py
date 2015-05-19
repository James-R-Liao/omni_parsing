__author__ = 'james_liao'

from  pkt_parsing  import  pkt_info_parsing

filein = open(r'D:\Personal_Study\Work_By_Myself\Modify_No_Rx_But_Rx_Abnormal.txt','rb')
#filein = open(r'D:\Personal_Study\Work_By_Myself\puhuo1_part1.txt','rb')
pattern = '2020202020706B7473' #9*2
data = filein.read()
pat_idx = data.find(pattern)

frt_pkt_idx = pat_idx + 30 #(9+6)*2
##################For Test############################
#print pat_idx
#print data[pat_idx:frt_pkt_idx] #start of first packet
#print data[frt_pkt_idx:frt_pkt_idx+128*2]
######################################################
pkt_info_parsing(data, frt_pkt_idx, 2)