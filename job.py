#!/usr/bin/python2
import htcondor
import classad
import os
import errno
import time

working_dir = 'condor6'
if os.path.exists(working_dir):
	filenames = os.listdir(working_dir)
	for filename in filenames:
		os.remove(working_dir + '/' + filename)
	os.rmdir(working_dir)
time.sleep(1)
os.makedirs(working_dir)
os.rename('./analyt_mod', working_dir + '/analyt_mod')
time.sleep(1)
os.chdir(working_dir)
schedd = htcondor.Schedd()
Tslot_max = 246140.0

p = [0.0, 0.5]
q = 1.0
M = [32, 64, 100]
Traw = [500.0 + i * 120.0 for i in range(2048)]

for ip in p:
	for iM in M:
		for iTraw in Traw:
			b = True
			while b:
				f = os.fork()
				if f: # parent
					r = os.wait()
					if not r[1]:
						b = False
				else: # child
					cmd = 'Glambda_Opt_AN_{}_{}_{}_{}'.format(str(iM), str(iTraw), str(ip), str(q))
					print(cmd)
					ad = classad.ClassAd({
						'Cmd' : './analyt_mod',
						'Arguments' : '{}'.format(cmd), 
						'UserLog' : cmd + '.log', 
						'Out' : cmd + '.out', 
						'Err' : cmd + '.err', 
						'ShouldTransferFiles' : 'YES'})
					schedd.submit(ad)
					os._exit(0)
