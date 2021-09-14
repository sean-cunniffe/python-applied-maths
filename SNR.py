import math as m

capacity = int(input("What is the channel capacity? (bits/s)"))
bandwidth = int(input("What is the bandwidth? (hertz)"))
sn = m.pow(2, capacity / bandwidth) - 1
ratio_in_db = 10 * (m.log(sn, 10))
print('SNR = %f db' % ratio_in_db)
