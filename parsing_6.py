__author__ = 'james_liao'

infile = open(r'D:\Personal_Study\Work_By_Myself\puhuo1.txt','rb')
outfile = open(r'D:\Personal_Study\Work_By_Myself\puhuo1_part1.txt','wb')


buffer = infile.read(500000)

outfile.write(buffer)

