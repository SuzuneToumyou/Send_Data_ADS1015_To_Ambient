#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import datetime
import ambient
import Adafruit_ADS1x15

ID = ****
writeKey = "****"

ambi = ambient.Ambient(ID,writeKey)
adc = Adafruit_ADS1x15.ADS1015()

GAIN = 1
sps = 250

msg = []

# LOOP
ii = 0
roop_cy = 499
for a in range(roop_cy):

	tmsg = {'created': str(datetime.datetime.now()), 'd1': adc.read_adc(0, gain=GAIN, data_rate=sps)}
	msg.append(tmsg)
	#time.sleep(0.05)

sent = ambi.send(msg)
sent.close()
