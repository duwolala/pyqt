#!/usr/bin/env python

'''
Data:2012.08.31         
'''

#############################
import os
import time
import sys
from epics import caget,caput
#############################


#TRX=blcMotor('Keithley6485:Measure')
UserFilename=caget('X16B1:EH:Keithley6485:UserFilename.VAL')
Samplename=caget('X16B1:EH:Keithley6485:Samplename.VAL')
#stop=blcMotor('')
#Note=blcMotor('')


#change directory and create user's file
save_dir='/home/marccd/Desktop/UserData/'
#os.chdir(save_dir)
##save_user_file_name=os.mkdir(UFn)

#print save_dir

save_time=time.strftime('%Y-%m-%d   %H:%M:%S')
save_time1=time.strftime('%Y-%m-%d')

if not os.path.exists(save_dir+save_time1+' '+UserFilename):
	os.mkdir(save_dir+save_time1+' '+UserFilename)

f=file(save_dir+save_time1+' '+UserFilename+'/'+save_time+' '+Samplename,'a')
caput('X16B1:EH:Keithley6485:Note','saving...')

caput('X16B1:EH:Keithley6485:Stop',0)

while caget('X16B1:EH:Keithley6485:Stop.VAL')==0:
	t=time.strftime('%H:%M:%S',time.localtime())
	current1=caget('X16B1:EH:Keithley6485_0:Measure.VAL')
	current2=caget('X16B1:EH:Keithley6485_1:Measure.VAL')
	f.write(t+'   '+str(current1)+'   '+str(current2)+'   '+'\n')
	#f.write(t+'   '+str(current1)+'   '+'\n')
	time.sleep(0.1)
f.close()

caput('X16B1:EH:Keithley6485:Note','Data saving has finished.')
time.sleep(1)
caput('X16B1:EH:Keithley6485:Note','')
sys.exit()



