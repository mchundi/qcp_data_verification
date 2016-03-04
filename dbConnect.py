from cassandra.cluster import Cluster
from cassandra.query import tuple_factory
from dbCheck import verifyDB

#DB Connection to leopold.mediamelon.com
def connectDB(serverIP,keySpace,customerId):
    print 'in connectDB'
    cluster = Cluster(contact_points = [serverIP],port=9042)
    session = cluster.connect(keySpace)
    session.row_factory = tuple_factory
    verifyDB(session,customerId)
    session.shutdown()
    cluster.shutdown()
    print 'returning from connectDB';

