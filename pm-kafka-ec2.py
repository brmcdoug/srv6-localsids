from kafka import KafkaConsumer
from arango import ArangoClient
import json 
from json import loads
import re

# define Kafka consumer and topic to monitor
consumer = KafkaConsumer(
    'jalapeno.pm',
     bootstrap_servers=['172.30.106.142:30092'],
     auto_offset_reset='latest',
     enable_auto_commit=False,
     group_id='jalapeno',
     max_poll_records=100,
     value_deserializer=lambda x: loads(x.decode('utf-8')))

print('List of topics: ', consumer.topics())

# for loop subscribes to Kafka messages and uploads docs to DB
print("starting loop")
for message in consumer:
    consumer.commit() 
    message = message.value
    msgobj = json.dumps(message, indent=4)
    print(msgobj)
    # beware, regex'ing follows
    msg = msgobj.replace("/", "_" )
    # msg = (re.sub("sid_context_key_u_dt4_u_dt_base_ctx_table_id", "table_id", msg))
    # msg = (re.sub("sid_context_key_u_dt6_u_dt_base_ctx_table_id", "table_id", msg))
    
    # convert json string to dict
    msgdict = json.loads(msg)
    interface = msgdict['tags']['interface_name']
    node_name = msgdict['tags']['source']
    #print(name, sid)

    # generate DB ID and Key
    key = node_name + "_" + interface
    #id = "srv6_local_sids/" + key
    msgdict['_key'] = key
    print("key", key)
    


