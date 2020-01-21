# Import the libs
import os
import urllib.request
import sched, time
import datetime

# Change the WD
os.chdir("/home/pi/Documents/NC_TCs")

#Mirlo, Ocracoke, and Hatteras URLs
Murl = "https://tims.ncdot.gov/TIMS/cameras/viewimage.ashx?id=NC12_MirloBeach.jpg"
Ourl = "https://tims.ncdot.gov/TIMS/cameras/viewimage.ashx?id=NC12_OcracokeNorth.jpg"
Hurl = "https://tims.ncdot.gov/TIMS/cameras/viewimage.ashx?id=NC12_NorthHatterasVillage.jpg"
Burl = "https://tims.ncdot.gov/TIMS/cameras/viewimage.ashx?id=NC12_Buxton.jpg"
Nurl =  "https://tims.ncdot.gov/TIMS/cameras/viewimage.ashx?id=NC12_NewInlet.jpg"
Aurl = "https://tims.ncdot.gov/TIMS/cameras/viewimage.ashx?id=NC12_CanalZone.jpg"

#Minute delay
Min = 10


#The function for the cameras
def GetTraffic():
    print ("looking at traffic...%s" % datetime.datetime.now())
    
    # get the images and save them
    urllib.request.urlretrieve(Murl, "Mdummy.jpg")
    urllib.request.urlretrieve(Ourl, "Odummy.jpg")
    urllib.request.urlretrieve(Hurl, "Hdummy.jpg")
    urllib.request.urlretrieve(Burl, "Bdummy.jpg")
    urllib.request.urlretrieve(Nurl, "Ndummy.jpg")
    urllib.request.urlretrieve(Aurl, "Adummy.jpg")
    
    #rename Mirlo   
    Mold = 'Mdummy.jpg'
    Mnew = 'Mirlo/%s-Mirlo.jpg' % datetime.datetime.now()
    os.rename(Mold, Mnew)
    
    #rename Ocracoke
    Oold = 'Odummy.jpg'
    Onew = 'Ocracoke/%s-Ocracoke.jpg' % datetime.datetime.now()
    os.rename(Oold, Onew)
    
    #rename hatteras
    Hold = 'Hdummy.jpg'
    Hnew = 'Hatteras/%s-Hatteras.jpg' % datetime.datetime.now()
    os.rename(Hold, Hnew)
    
        #rename buxton
    Bold = 'Bdummy.jpg'
    Bnew = 'Buxton/%s-Buxton.jpg' % datetime.datetime.now()
    os.rename(Bold, Bnew)
    
    #rename new inlet
    Nold = 'Ndummy.jpg'
    Nnew = 'NewInlet/%s-NewInlet.jpg' % datetime.datetime.now()
    os.rename(Nold, Nnew)
    
    #rename canal zone
    Aold = 'Adummy.jpg'
    Anew = 'Canal/%s-Canal.jpg' % datetime.datetime.now()
    os.rename(Aold, Anew)
    
#schedule
scheduler = sched.scheduler(time.time, time.sleep)
scheduler.enter(0, 1, GetTraffic, ())

#loop to make it go
while True:
    scheduler.run()
    scheduler.enter(Min*60, 1, GetTraffic, ())





