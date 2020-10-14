import time

def _time():
    t = time.gmtime(time.time())
    y=t.tm_year
    d=t.tm_yday-1
    h=t.tm_hour+8
    m=t.tm_min
    s=t.tm_sec
    if y%400==0:
        dy=366
    elif y%100==0:
        dy=365
    elif y%4==0:
        dy=366
    else:
        dy=365
    dys=dy*24*60*60
    return(str(y)+"已過了"+str((d*24*60*60+h*60*60+m*60+s)/dys*100)+"%")