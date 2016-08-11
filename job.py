#!/usr/bin/python2
import htcondor
import classad
import os
import errno
import time

working_dir = 'condor_test'
if os.path.exists(working_dir):
	filenames = os.listdir(working_dir)
	for filename in filenames:
		os.remove(working_dir + '/' + filename)
	os.rmdir(working_dir)
time.sleep(1)
os.makedirs(working_dir)
os.rename('./test', working_dir + '/test')
time.sleep(1)
os.chdir(working_dir)
schedd = htcondor.Schedd()

args = [str(i) for i in range(100000)]

for iarg in args:
	b = True
	while b:
		f = os.fork()
		if f: # parent
			r = os.wait()
			if not r[1]:
				b = False
		else: # child
			cmd = '{}'.format(iarg)
			print(cmd)
			ad = classad.ClassAd({
				'Cmd' : './test',
				'Arguments' : '{}'.format(cmd), 
				'UserLog' : cmd + '.log', 
				'Out' : cmd + '.out', 
				'Err' : cmd + '.err', 
				'ShouldTransferFiles' : 'YES'})
			schedd.submit(ad)
			os._exit(0)
