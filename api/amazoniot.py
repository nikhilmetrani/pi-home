#!/usr/bin/python

# Copyright ISS, NUS 2016

import paho.mqtt.client as paho
import os
import socket
import ssl
from time import sleep
from random import uniform

mqttc = paho.Client()


def on_connect_delegate(delegate):
    mqttc.on_connect = delegate


def on_message_delegate(delegate):
    mqttc.on_message = delegate


def publish(topic, message, qos=1):
    mqttc.publish(topic, message, qos=1)

def init(rootca, certfile, keyfile, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None):
    mqttc.tls_set(rootca, certfile=certfile, keyfile=keyfile, cert_reqs=cert_reqs, tls_version=tls_version, ciphers=ciphers)


def connect(awshost, awsport, keepalive=60):
    mqttc.connect(awshost, awsport, keepalive=keepalive)


def loop_start():
    mqttc.loop_start()


def loop_forever():
    mqttc.loop_forever()


def subscribe(topic="#", qos=1):
    mqttc.subscribe(topic, qos=qos)

if "__main__" == __name__:
    print("File must be imported.")

