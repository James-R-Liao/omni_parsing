__author__ = 'james_liao'

infile = open(r'D:\Personal_Study\Work_By_Myself\Modify_No_Rx_But_Rx_Abnormal.pkt','rb')
outfile = open(r'D:\Personal_Study\Work_By_Myself\test_read_Rx_Abnomral_9.txt','wb')
cnt = 0

while 1:
    c = infile.read(1)
    if not c:
        break
    cnt = cnt + 1
    #outfile.write(hex(ord(c))- '0x')
    temp = ord(c)
    if temp < 16 :
        outfile.write('0'+"%X"%temp)
    else:
        outfile.write("%X"%temp)
    outfile.write(' ')
    if (cnt%16 == 0):
        outfile.write('\r\n')

outfile .close()
infile.close()



