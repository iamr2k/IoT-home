import boto3
# client = boto3.client('iot')
# response = client.describe_thing(
#     thingName='RaspiHome'
# )

# print(response)

iot_client = boto3.client('iot-data')
topic = "test/testing"
iot_client.publish(topic=topic, payload="""{
  "message": "Hello World!",
  "sequence": 7
}""")
res = iot_client.subscribe(topic=topic, qos=1)
print(res)
