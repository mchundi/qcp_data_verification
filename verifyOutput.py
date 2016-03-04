import json


def verifyClientInfo(clientInfo):
    print "In VerifyClientInfo"
    
    data = "clientdata(country=u'India', city=u'Bangalore', region=u'Karnataka', isp=u'', latitude=12.9833, longitude=77.5833, ipaddress=u'122.167.174.57', uahash=1454340201, cdn=u'Mojohost')"
        
    if clientInfo == data:
        print "ClientInfo is correct"
    else:
        print "ClientInfo is wrong!!"
    
    print "Returning from verifyClientInfo"
    return True;

def verifyDeviceInfo(deviceInfo):
    data = "devicedata(platform=u'Unknown', device=u'unknown', brand=u'Unknown', networktype=u'', model=u'Unknown', scrnres=u'', sdkversion=u'')"
    
    if deviceInfo == data:
        print "deviceInfo is correct"
    else:
        print "deviceInfo is wrong!!"
    
    return True;


def verifyStreamInfo(streamInfo):
    data = "streamdata(maxres=u'720p', minres=u'720p', maxfps=24.0, minfps=24.0, numofprofile=6, totalduration=260.29, streamformat=u'MPEG-DASH', islive=False)"
    
    if streamInfo == data:
        print "streamInfo is correct"
    else:
        print "streamInfo is wrong!!"
    
    return True;



def verifyQualityInfo(qualityInfo):
    data = "qualitydata(maxqualimp=0.0, countqualimp=0, minqualcbr=0.9, minqualqbr=0.9, sumqualqbr=56.3999, sumqualcbr=56.3999, varqualcbr=144.2607, qualcbr=2.6857, qualqbr=2.6857, qualcbrsum2=3180.9487, qualqbrsum2=3180.9487, pctqualvarred=0.0, varqualqbr=144.2607)"
    
    if qualityInfo == data:
        print "qualityInfo is correct"
    else:
        print "qualityInfo is wrong!!"
    
    return True;



def verifyQOEInfo(qoedataInfo):
    data = "qoedata(frameloss=0, latency=1972.0, bandwidth=38364.44107368422, buffwait=0.0, sumframeloss=0, sumbandwidth=728924.3804000001, sumbuffwait=0.0, sumlatency=1972.0)"
    
    if qoedataInfo == data:
        print "qoedataInfo is correct"
    else:
        print "qoedataInfo is wrong!!"
    
    return True;