from urllib2 import Request,urlopen
import json

#Send JSON POST request ot StreamProducer
def sendPayload(data):
    print 'in Sendpayload'
    print data
    url = 'http://99.192.203.99:80/StreamProducer'
    header = { 'Content-Type': 'application/json' }
    req = Request(url,data,header)
    response = urlopen(req)

    print (response.code)
    if response.code == 200:
        print 'Request sent successfully'
    else:
        print 'Request failed!!'
    print 'returning from sendpayload'
    return;

def sendPlayerData(fileName):
    print "in sendPlayerData"
    #read the input file and store each line in a list
    data = []
    with open(fileName) as f:
        for line in f:
            data.append(json.loads(line))
            
    #generate the request
    url = 'http://99.192.203.99:80/StreamProducer'
    header = { 'Content-Type': 'application/json' }

    #convert each line of input file as string before sending the request
    i=0
    sendCount=0
    while i != len(data):
        inStr  = json.dumps(data[i]) 
        print inStr
        print type(inStr)
        req = Request(url,inStr,header)
        response = urlopen(req)

        print (response.code)
        if response.code == 200:
            sendCount += 1
    i += 1
    
    if sendCount == len(data):
        print "Request sent successfully"
    else:
        print "Request failed!!!"
        
    print"returning from sendPlayerData"
    
    return;