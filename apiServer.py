from urllib2 import Request,urlopen
import json
from time import time


#onboard a customer with the details in onBoard.json file and return the customer ID
def onBoarding(onBoardForm):
    
    print "in APISERVER"
    print onBoardForm
    
    tic = time()
    url = 'http://vickers.mediamelon.com:7878/mm-apis/onboard'
    header = { 'Content-Type': 'application/json' }
    req = Request(url,onBoardForm,header)
    response = urlopen(req)
    toc = time()
        
    print "Execution time: {0}" .format(toc-tic)
    responseJSON = json.load(response)

    customerID = int(json.dumps(responseJSON['custID']))
    print (response.code)
    if response.code == 200:
        print 'Request sent successfully'
    else:
        print 'Request failed!!'
    
    print customerID
    print 'returning from APISERVER'
    return customerID;

def getAudienceData(customerId):
    
    url = 'http://vickers.mediamelon.com:7878/mm-apis/qbrData/audience/'+str(customerId)
    audienceData = getData(url)
    print "Audience data: {0}" .format(audienceData);


def getVodAssetData(customerId,period):
    url = 'http://vickers.mediamelon.com:7878/mm-apis/qbrData/vod/'+str(customerId)+'?'+period+'=minute&dimension=asset'
    vodAssetData = getData(url)
    print "VodAssetData"+period+": {0}" .format(vodAssetData);
    
def getDashboardQueryData(customerId):
    #buffTime
    buffTimeURL = 'http://vickers.mediamelon.com:7878/mm-apis/qbrData/vod/'+str(customerId)+'?period=minute&metrics=assetid%2Csumbuffwait&dimension=asset'
    buffTime = getData(buffTimeURL)
    print "BuffTime: {0}" .format(buffTime)
    
    startLatencyURL = 'http://vickers.mediamelon.com:7878/mm-apis/qbrData/vod/'+str(customerId)+'?period=hour&metrics=assetid%2Clatency&dimension=asset'
    startLatency = getData(startLatencyURL)
    print "startLatency: {0}" .format(startLatency)
    
    avgBitRateURL = 'http://vickers.mediamelon.com:7878/mm-apis/qbrData/vod/'+str(customerId)+'?period=minute&metrics=assetid%2C%20qbrbitrate&dimension=asset'
    avgBitRate = getData(avgBitRateURL)
    print "avgBitRate: {0}" .format(avgBitRate)
    
    avgBufferingURL = 'http://vickers.mediamelon.com:7878/mm-apis/qbrData/vod/'+str(customerId)+'?period=minute&metrics=buffwait%2Cassetid&dimension=asset'
    avgBuffering = getData(avgBufferingURL)
    print "avgBuffering: {0}" .format(avgBuffering)
    
    buffDurationURL = 'http://vickers.mediamelon.com:7878/mm-apis/qbrData/vod/'+str(customerId)+'?period=minute&metrics=assetid%2C%20sumbuffwait&dimension=asset'
    buffDuration = getData(buffDurationURL)
    print "buffDuration: {0}" .format(buffDuration)
    
    buffEventsURL = 'http://vickers.mediamelon.com:7878/mm-apis/qbrData/vod/'+str(customerId)+'?period=minute&metrics=buffwait&dimension=asset'
    buffEvents = getData(buffEventsURL)
    print "buffEvents: {0}" .format(buffEvents)
    
    bandwidthPerISPURL = 'http://vickers.mediamelon.com:7878/mm-apis/qbrData/vod/'+str(customerId)+'?period=minute&metrics=bandwidth&dimension=country%2Cisp'
    bandwidthPerISP = getData(bandwidthPerISPURL)
    print "bandwidthPerISP: {0}" .format(bandwidthPerISP)
    
    avgBuffCdnURL = 'http://vickers.mediamelon.com:7878/mm-apis/qbrData/vod/'+str(customerId)+'?period=minute&metrics=buffwait&dimension=country%2Ccdn'
    avgBuffCdn = getData(avgBuffCdnURL)
    print "avgBuffCdn: {0}" .format(avgBuffCdn)
    
    
    
def getData(url):
    request = Request(url)
    request.add_header('Content-Type', 'application/json')
    
    tic = time()
    response = urlopen(request)
        
    json_raw= response.readlines()
    json_object = json.loads(json_raw[0])
    toc = time()
        
    print "Execution time: {0}" .format(toc-tic)
    return json.dumps(json_object);