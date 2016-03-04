import json,traceback,time
from verifyOutput import verifyClientInfo,verifyDeviceInfo, verifyStreamInfo, verifyQOEInfo,verifyQualityInfo

audienceData = 0
clientInfo = ""
deviceInfo = ""
streamInfo = ""
qoedataInfo = ""
qualityInfo = ""

def verifyDB(session,customerId):
    print 'in verifyDB'
    
    #Analyzer waits for about a minute before processing a batch of data
    #wait for 60 seconds before verifying DB
    print "waiting for 60 seconds"
    time.sleep(60)
    try:
        tic = time.time()
        minuteData = (session.execute("select count(*) from audience_data_minute where custid={0}" .format(customerId)))[0][0]
        toc = time.time()
        
        print "Execution time: {0}" .format(toc-tic)
            
        if minuteData == 0:
            print "wait for hour to populate data in hour tables"
            time.sleep(3000)
            verifyHourTables(session,customerId)
        else:
            print "will verify minute tables"
            verifyMinuteTables(session,customerId)
           
    except Exception:
        print "Oops!  Something is wrong with the queries"
        traceback.print_exc()
       
    print 'returning from verifyDB';

def verifyHourTables(session,customerId):
    print "in hour table verification"
    #verify data in hour tables
    try:
        tic = time.time()
        result = session.execute("select * from vod_asset_data_hour where custid={0}" .format(customerId)) 
        toc = time.time()
        
        print "Execution time: {0}" .format(toc-tic)
        if result:
            streamInfo =  str(result[0][9])
            qoedataInfo = str(result[0][6])
            qualityInfo = str(result[0][7])
        
            verifyStreamInfo(streamInfo)
            verifyQOEInfo(qoedataInfo)
            verifyQualityInfo(qualityInfo)
        else:
            print "no data in hour table"
                
    except Exception:
        print "Oops!  Something is wrong with the hour table queries"
        traceback.print_exc()
        
    print "returning from verifyHourTables" ;   
    #return status;

def verifyMinuteTables(session,customerId):
    print "in minute tables verification"
    #verify data in hour tables
    try:
        tic = time.time()
        result = session.execute("select * from vod_asset_data_minute where custid={0}" .format(customerId))
        toc = time.time()
        
        print "Execution time: {0}" .format(toc-tic) 
        if result:
            
            streamInfo =  str(result[0][9])
            qoedataInfo = str(result[0][6])
            qualityInfo = str(result[0][7])
        
            verifyStreamInfo(streamInfo)
            verifyQOEInfo(qoedataInfo)
            verifyQualityInfo(qualityInfo)
        else:
            print "No data in minute table"
    
    except Exception:
        print "Oops!  Something is wrong with the minute table queries"
        traceback.print_exc()
         
    print "returning from verifyMinuteTables" ;
            
