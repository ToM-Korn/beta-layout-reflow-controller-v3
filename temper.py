# python keep warm for reflow

import serial
import sys
import time
import re

s = None

def initOven():
    for x in range(0,3):
        try:
            s = serial.Serial("/dev/ttyUSB"+str(x),9600,timeout=1)
            s.write(b'manual 1\r')
            s.readall()
            temp = getTemp()
            if isinstance(temp,int):
                return
        except:
            pass

def getTemp():
    s.write(b'tempshow\r')
    serial_text = s.readall()
    matches = re.findall('\+\s?(\d+),?',serial_text)
    if matches:
        return int(matches[-1])
    else:
        raise Exception('NO VALID TEMPERATURE RETURNED!!')


def keepWarm(target_temp,rf_time):
    seconds = rf_time * 60
    start = time.time()

    end = start + 1000 # only for preheat

    # print serial_text ### DEBUG
    cur_temp = getTemp()

    print 'current temp: +',str(cur_temp),'C'
    print 'starting keep warm at:',str(target_temp),'C for',str(rf_time),'minutes.'


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

        cur_temp = getTemp()
        if cur_temp < target_temp and preheat == True:
            print 'preheat - current temp: +'+str(cur_temp)+'C'
        else: 
            preheat = False
            end = start + seconds
        if preheat == False:
            print 'current temperature: +'+str(cur_temp)+'C','time to go in s:',str(int(end-time.time()))

    # cooldown starts here
    # cooldown is same like seconds but the temp between target_temp and 20 degrees need to be equally tiled
    total_degrees = target_temp - 25
    degree_by_seconds = seconds / total_degrees # this is the time in seconds the oven should reduce by one degree

    current_target = target_temp-1

    while current_target > 25:
        end = time.time() + degree_by_seconds
        cur_temp = getTemp()
        while time.time() < end:
            if cur_temp < current_target -10:
                for x in range(0,10):
                    s.write(b'shot 100\r')
                    time.sleep(1)
            elif cur_temp < current_target-3:
                s.write(b'shot 50\r')
            elif cur_temp < current_target:
                s.write(b'shot 30\r')
            elif cur_temp >= current_target:
                time.sleep(3)
                s.write(b'tempshow\r')
            cur_temp = getTemp()
            print 'current Temperature: +'+str(cur_temp)+'C'
            print ' target Temperature: +'+str(current_target)+'C'
            print 'time to go in s:',str(int(end-time.time()))
            print
        current_target -= 1

if __name__ == '__main__':
    print 'Usage: python temper.py thickness_of_pmma(in mm)'
    temp = 0
    rf_time = 0
    try:
        temp = 85 # this is what is adviced for pmma
        plate_mm = int(sys.argv[1]) # comes from user
        rf_time = plate_mm * 60 # plate thickness times 60 minutes
    except:
        pass
    keepWarm(temp,rf_time)