# Import the libs
import os
import urllib.request
import sched, time
import datetime

# Change the WD
os.chdir("/home/pi/Documents/NC_TCs")

#Mirlo, Ocracoke, and Hatteras URLs
Murl = "https://tims.ncdot.gov/TIMS/cameras/viewimage.ashx?id=NC12_Mirlo_Beach.jpg"
Ourl = "https://tims.ncdot.gov/TIMS/cameras/viewimage.ashx?id=NC12_Ocracoke_North.jpg"
Hurl = "https://tims.ncdot.gov/TIMS/cameras/viewimage.ashx?id=NC12_North_Hatteras_Village.jpg"

#Minute delay
Min = 10


#The function for the cameras
def GetTraffic():
    print ("looking at traffic...%s" % datetime.datetime.now())
    
    # get the images and save them
    urllib.request.urlretrieve(Murl, "Mdummy.jpg")
    urllib.request.urlretrieve(Ourl, "Odummy.jpg")
    urllib.request.urlretrieve(Hurl, "Hdummy.jpg")
    
    #rename
    Mold = 'Mdummy.jpg'
    Mnew = 'Mirlo/%s-Mirlo.jpg' % datetime.datetime.now()
    os.rename(Mold, Mnew)
    
    #rename
    Oold = 'Odummy.jpg'
    Onew = 'Ocracoke/%s-Ocracoke.jpg' % datetime.datetime.now()
    os.rename(Oold, Onew)
    
    #rename
    Hold = 'Hdummy.jpg'
    Hnew = 'Hatteras/%s-Hatteras.jpg' % datetime.datetime.now()
    os.rename(Hold, Hnew)
    
#schedule
scheduler = sched.scheduler(time.time, time.sleep)
scheduler.enter(0, 1, GetTraffic, ())

#loop to make it go
while True:
    scheduler.run()
    scheduler.enter(Min*60, 1, GetTraffic, ())



