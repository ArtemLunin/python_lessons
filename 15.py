import os
import subprocess
import psutil

# id текущего процесса
print(os.getpid())
# current dir
print(os.getcwd())
# system info
print(os.uname())
print(os.getloadavg())
# aka console
os.system('date -u')

#running shell command
ret = subprocess.getoutput('date -u | wc')
print(ret)
ret = subprocess.check_output(['date', '-u'])
print(ret)
#with status
ret = subprocess.getstatusoutput('date')
# only status
ret = subprocess.call('date')
print(ret)
#with arguments, output to screen
subprocess.call('date -u', shell=True)
# or
subprocess.call(['date', '-u'])

# cpu load info
print(psutil.cpu_times(True))
print(psutil.cpu_percent(True))
