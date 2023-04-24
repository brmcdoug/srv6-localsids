from kafka import KafkaConsumer
from arango import ArangoClient
import json 
from json import loads
import re

# define Kafka consumer and topic to monitor
consumer = KafkaConsumer(
    'jalapeno.pm',
     bootstrap_servers=['52.11.224.254:30092'],
     auto_offset_reset='latest',
     enable_auto_commit=False,
     group_id='jalapeno',
     max_poll_records=100,
     value_deserializer=lambda x: loads(x.decode('utf-8')))

print('Available topics to consume: ', consumer.topics())

# for loop subscribes to Kafka messages and uploads docs to DB
print("starting loop")
for message in consumer:
    consumer.commit() 
    message = message.value
    msgobj = json.dumps(message, indent=4)
    print("msgobj", msgobj)
    # beware, regex'ing follows
    msg = msgobj.replace("/", "_" )
    msg = (re.sub("sid_context_key_u_dt4_u_dt_base_ctx_table_id", "table_id", msg))
    msg = (re.sub("sid_context_key_u_dt6_u_dt_base_ctx_table_id", "table_id", msg))
    
    # convert json string to dict
    msgdict = json.loads(msg)
    sid = msgdict['fields']['sid']
    name = msgdict['tags']['source']
    #print(name, sid)

    # generate DB ID and Key
    key = name + "_" + sid
    id = "srv6_local_sids/" + key
    msgdict['_key'] = key

    # upload document to DB
    if db.has_document(id):
        metadata = srv6_local_sids.update(msgdict)
        print("document exists, updating timestamp: ", id)
    else:
        metadata = srv6_local_sids.insert(msgdict)
    
        print("document added: ", msgdict['_key'])

