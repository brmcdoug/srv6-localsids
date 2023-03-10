# srv6-localsids
A demo Jalapeno data processor which subscribes to Kafka jalapeno.srv6 topic, grabs srv6-localsids data from the topic and writes the data to ArangoDB srv6_local_sids collection.

1. Configure IOS-XR streaming telemetry. As of XR 7.8.1 there is no Event Driven Telemetry (EDT) for srv6 sids, so in this example we use MDT and stream the data every 120 seconds
   
```
telemetry model-driven
 sensor-group srv6-sid
  sensor-path Cisco-IOS-XR-segment-routing-srv6-oper:srv6/active/locator-all-sids/locator-all-sid
 !
 subscription base_metrics
  sensor-group-id srv6-sid sample-interval 120000

commit
```
2. Replace Jalapeno's default Telegraf MDT collector config with this one:
   ![Telegraf](./telegraf_ingress_cfg.yaml)

3. Deploy the srv6-localsids processor

```
kubectl create -f srv6_localsids_dp.yaml
```
