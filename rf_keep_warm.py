# python keep warm for reflow

import serial
import sys
import time
import re

s = serial.Serial("/dev/ttyUSB1",9600,timeout=1)


def getTemp(serial_text):
	matches = re.findall('\+\s?(\d+),?',serial_text)
	if matches:
		return matches[-1]
	else:
		raise Exception('NO VALID TEMPERATURE RETURNED!!')

def keepWarm(target_temp,rf_time):
	s.write(b'manual 1\r')
	s.readall()
	seconds = rf_time * 60
	start = time.time()

	end = start + 1000 # only for preheat

	s.write(b'tempshow\r')
	serial_text = s.readall()
	# print serial_text ### DEBUG
	cur_temp = getTemp(serial_text)

	print 'current temp: +',cur_temp,'C'
	print 'starting keep warm at:',target_temp,'C for',rf_time,'minutes.'

	cur_temp = int(cur_temp)

	preheat = True

	while time.time() < end:
		if cur_temp < target_temp -10:
			for x in range(0,10):
				s.write(b'shot 100\r')
				time.sleep(1)
		elif cur_temp < target_temp-3:
			s.write(b'shot 50\r')
		elif cur_temp < target_temp:
			s.write(b'shot 30\r')
		elif cur_temp >= target_temp:
			time.sleep(3)
			s.write(b'tempshow\r')

		serial_text = s.readall()
		# print serial_text ### DEBUG
		if serial_text != '':
			cur_temp = getTemp(serial_text)
			cur_temp = int(cur_temp)
		if cur_temp < target_temp and preheat == True:
			print 'preheat - current temp: +'+str(cur_temp)+'C'
		else: 
			preheat = False
			end = start + seconds
		if preheat == False:
			print 'current temperature: +'+str(cur_temp)+'C','time to go in s:',str(int(end-time.time()))

if __name__ == '__main__':
	print 'Usage: python rf_keep_warm temp(in C) time(in min)'
	temp = 60
	rf_time = 15
	try:
		temp = int(sys.argv[1])
		rf_time = int(sys.argv[2])
	except:
		pass
	keepWarm(temp,rf_time)