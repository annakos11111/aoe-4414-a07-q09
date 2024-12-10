# max_bitrate.py
#
# Usage: python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz
# 
# Parameters:
# tx_w          : power in watts
# tx_gain_db    : transmitter gain in db
# freq_hz       : frequemcy
# dist_km       : distance
# rx_gain_db    : reciever gain in db
# n0_j          : noise spectral density in Joules
# bw_hz         : channel bandwidth
# 
# Output:
# r_max
#
# Written by Anna Kosnic
#
# import Python modules
import sys # argv
import math as m

# "constants"
c = 2.99792458*10**8


# initialize script arguments
tx_w        = float('nan')
tx_gain_db  = float('nan')
freq_hz     = float('nan')
dist_km     = float('nan')
rx_gain_db  = float('nan')
n0_j        = float('nan')
bw_hz       = float('nan')

# parse script arguments
if len(sys.argv)==8:
    tx_w        = float(sys.argv[1])
    tx_gain_db  = float(sys.argv[2])
    freq_hz     = float(sys.argv[3])
    dist_km     = float(sys.argv[4])
    rx_gain_db  = float(sys.argv[5])
    n0_j        = float(sys.argv[6])
    bw_hz       = float(sys.argv[7])
else:
    print(\
        'Usage: '\
        'python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz'\
            )
    exit()


# write script below this line
lam = c/freq_hz
Gt = 10**(tx_gain_db/10)
Gr = 10**(rx_gain_db/10)
dist = dist_km*1000
Ll = 10**(-1/10)

C = tx_w*Ll*Gt*(lam/(4*m.pi*dist))**2*Gr
N = n0_j*bw_hz

r_max = bw_hz*m.log2(1+C/N)
print(m.floor(r_max))