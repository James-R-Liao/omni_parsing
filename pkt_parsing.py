__author__ = 'Administrator'

def get_field(dat_str, sat_idx, fid_offset_idx, byt_leg):# fid_offset_idx = 4(low num), byt_leg = 2

    fid_idx = sat_idx + fid_offset_idx*2
    temp_idx = range(byt_leg)
    temp_idx.reverse()
    fid_str = ''
    for i in temp_idx: #[1,0]
        fid_str += dat_str[fid_idx+i*2:fid_idx+i*2+2]
    #print fid_str
    fid_dec = int(fid_str, 16)
    return fid_dec


def pkt_info_parsing(dat_str, sat_idx, pkt_num): #,flag_MCS

    pkt_length = []
    phy_rate = []
    for i in range(pkt_num):
        #print sat_idx,dat_str[sat_idx:sat_idx+128*2]
        pkt_length.append(get_field(dat_str, sat_idx, 4, 4))
        phy_rate.append(get_field(dat_str, sat_idx, int('28',16), 2)/2)
        pkt_length_actual = get_field(dat_str, sat_idx, int('7c',16), 4)

        print "%dth pkt length: %d" % (i+1,pkt_length[i])
        print "%dth phy rate: %d Mbps" %(i+1,phy_rate[i])
        #print "%dth pkt length_actual: %d" % (i, pkt_length_actual)
        print

        sat_idx = sat_idx + 126*2 + pkt_length_actual*2#next_pkt_idx
	
	
#def MCS_info_parsing() #according to the flag_MCS 	


		
		
		