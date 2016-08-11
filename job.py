#!/usr/bin/python2
import htcondor
import classad
import os
import errno
import time

working_dir = 'condor_test' # рабочая директория
if os.path.exists(working_dir): # если директория существует, удаляем её вместе со всеми файлами
	filenames = os.listdir(working_dir)
	for filename in filenames:
		os.remove(working_dir + '/' + filename)
	os.rmdir(working_dir)
time.sleep(1)
os.makedirs(working_dir) # создаём из рабочую директорию
os.rename('./test', working_dir + '/test') # переносим в директорию исполняемый файл
time.sleep(1)
os.chdir(working_dir) # работаем из рабочей директории
schedd = htcondor.Schedd()

args = [str(i) for i in range(100000)] # аргументы программы

for iarg in args:
	b = True # входим в бесконечный цикл
	while b:
		f = os.fork()
		if f: # родитель
			r = os.wait() # ждём выполнения дочернего процесса
			if not r[1]: # выполнение дочернего процесса завершилось без ошибок
				b = False # выходим из бесконечного цикла
		else: # дитя
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
