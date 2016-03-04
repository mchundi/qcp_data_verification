import time,json
from random import randint

def parseJSON( fileName,customerId ):
    print 'in parseJSON'
    
    json_data=open( fileName )
    data=json.load(json_data)

    #Change the timestamp of the payload to current time
    nowTime=int(time.time()*1000)
    
    data['timestamp']=nowTime
    data['qubitData'][0]['streamID']['custId']=customerId
    segInfoLen = len(data['qubitData'][0]['segInfo'])
    pbInfoLen = len(data['qubitData'][0]['pbInfo'])

    index=0
    for index in range(0, segInfoLen):
        data['qubitData'][0]['segInfo'][index]['timestamp']=nowTime
    index=0
    for index in range(0, pbInfoLen):
        data['qubitData'][0]['pbInfo'][index]['timestamp']=nowTime

    json_data.close()
    print'returning from parse JSON'
    return json.dumps(data);

def onboarForm(fileName):
    print 'in onBoarform parsing'
    json_data=open( fileName )
    data=json.load(json_data)
    
    randNum = str(randint(0,10))
    
    orgName = 'TestUser'+randNum
    orgWebsite = 'automation'+randNum+'.com'
    adminMail = 'testuser1@automation'+randNum+'.com'
    data['orgName'] = orgName
    data['orgWebsite'] = orgWebsite
    data['adminMail'] = adminMail
    
    #print json.dumps(data)
    json_data.close()
    print'returning from onboarForm'
    return json.dumps(data);

    
    
    


