from readInput import parseJSON,onboarForm
from kafkaTopicConsumer import kafkaConnection,consumerProducer,payloadConsumer,consumerProcessor
from dataPump import sendPayload
from dbConnect import connectDB
from apiServer import onBoarding,getAudienceData,getVodAssetData,getDashboardQueryData
from preRequisiteCheck import componentCheck
import sys

#verify if the required components are up and running. Else abort the test
if componentCheck():
    print "Pre-condition statisfied. Conitnuing with the test"
else:
    sys.exit("Pre-condition not satisfied. Aborting the test")
    
#onboard a new customer and prepare the input data
onboardFile = onboarForm('/sts/workspace/qcp/qcp_data_verification/onBoard.json')
customerId = onBoarding(onboardFile)
print ('customerID: %d' % customerId)

inputData = parseJSON('/sts/workspace/qcp/qcp_data_verification/input.json',customerId);
print ("input: {0}" .format(inputData))

#Connect to kafka cluster to read data
kafkaConnection();
streamProducer=consumerProducer();
streamProcessor=consumerProcessor();

#Send input data
sendPayload(inputData);

#Verify StreamProducer and processor topics for payloads
streamProducerData=payloadConsumer(streamProducer)
if streamProducerData == 1: 
    print "Input reached StreamProducer"
else:
    print "Either input did not reach StreamProducer or incorrect input reached StreamProducer"

streamProcessorData=payloadConsumer(streamProcessor)
if streamProcessorData == 65: 
    print "Input reached StreamProcessor"
else:
    print "Either input did not reach StreamProcessor or incorrect input reached StreamProcessor"
    

#Verify DB for aggregated data
connectDB('99.192.203.100','qbr_vod',customerId)

#APIServer data test
getAudienceData(507899387)
getVodAssetData(507899387,'hour')
getVodAssetData(507899387,'minute')
getVodAssetData(507899387,'day')

#Verify QoE Dashboard data
getDashboardQueryData(507899387)


print 'ProgramEnded!!'
