'''
/*
 * Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License").
 * You may not use this file except in compliance with the License.
 * A copy of the License is located at
 *
 *  http://aws.amazon.com/apache2.0
 *
 * or in the "license" file accompanying this file. This file is distributed
 * on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 * express or implied. See the License for the specific language governing
 * permissions and limitations under the License.
 */
 '''

import requests
from multiprocessing.reduction import ACKNOWLEDGE
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import time
import argparse
import json

AllowedActions = ['both', 'publish', 'subscribe']

# Custom MQTT message callback


def customCallback(client, userdata, message):
    print("Received a new message: ")
    print(json.loads(message.payload))
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")

import os
host = "adbxgzfkc7fye-ats.iot.ap-south-1.amazonaws.com"
rootCAPath = "/home/pi/rbk/temp/mqtt-cert/root-CA.crt"
certificatePath = "/home/pi/rbk/temp/mqtt-cert/RaspiHome.cert.pem"
privateKeyPath = "/home/pi/rbk/temp/mqtt-cert/RaspiHome.private.key"
port = 8883
useWebsocket = False
clientId = "basicPubSub"
topic = "sdk/test/Python"
mode = 'both'
u_message = "Hello from Raspberry!"

# Configure logging
logger = logging.getLogger("AWSIoTPythonSDK.core")
logger.setLevel(logging.DEBUG)
streamHandler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

# Init AWSIoTMQTTClient
myAWSIoTMQTTClient = None
if useWebsocket:
    myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId, useWebsocket=True)
    myAWSIoTMQTTClient.configureEndpoint(host, port)
    myAWSIoTMQTTClient.configureCredentials(rootCAPath)
else:
    myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
    myAWSIoTMQTTClient.configureEndpoint(host, port)
    myAWSIoTMQTTClient.configureCredentials(
        rootCAPath, privateKeyPath, certificatePath)

# AWSIoTMQTTClient connection configuration
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
# Infinite offline Publish queueing
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

# Connect and subscribe to AWS IoT
myAWSIoTMQTTClient.connect()
while True:
    if mode == 'both' or mode == 'subscribe':
        myAWSIoTMQTTClient.subscribe(topic, 1, customCallback)
    time.sleep(2)

# Publish to the same topic in a loop forever
loopCount = 0
if mode == 'both' or mode == 'publish':
    message = {}
    message['message'] = u_message
    message['sequence'] = loopCount
    messageJson = json.dumps(message)
    # myAWSIoTMQTTClient.publish(topic, messageJson, 1)
    # if mode == 'both':
    #     # print('Published topic %s: %s\n' % (topic, messageJson))
    # loopCount += 1


def ACK(*args, **kwargs):
    message = {}
    message['message'] = "message _recieved"
    message['sequence'] = loopCount
    messageJson = json.dumps(message)
    myAWSIoTMQTTClient.publish(topic, messageJson, 1)
    if mode == 'publish':
        print('Published topic %s: %s\n' % (topic, messageJson))
    return True


def on_message_received(topic, payload, **kwargs):
    print("Received message from topic '{}': {}".format(topic, payload))


# subscribe_future = myAWSIoTMQTTClient.subscribe(
#     topic="newd",
#     QoS=1,
#     callback=ACK
# )
# subscribe_result = subscribe_future.result()

# res = requests.get("https://3.110.34.167/v1/search/similar_products/")
# print(res.text)
