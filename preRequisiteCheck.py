import subprocess,re

#To verify if all the components are up and running

def findThisProcess( process_name,remoteServer ):
    command = "ssh "+remoteServer+" ps -eaf | grep "+process_name
    ps     = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    output = ps.stdout.read()
    ps.stdout.close()
    ps.wait()
    
    if output:
        print process_name+" is running"
    else:
        print process_name+" is not running"
    return output;

# This is the function you can use  
def isThisRunning( process_name ):
    output = findThisProcess( process_name )

    if re.search('path/of/process'+process_name, output) is None:
        return False;
    else:
        return True;


def componentCheck():
    
    print "in componentCheck"
    #status = False
    streamAnalyzer  = findThisProcess("StreamAnalyzer-0.0.1.jar","root@99.192.203.100")
    streamProcessor = findThisProcess("StreamProcessor-jar-with-dependencies.jar","root@99.192.203.103")
    apiServer = findThisProcess("APIServer-assembly-0.1.0-SNAPSHOT.jar","root@99.192.203.103")
    
    
    if streamProcessor and streamAnalyzer and apiServer:
        return True
    else:
        return False
        
     
    print "returning from componentCheck";
