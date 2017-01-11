#import os
#os.system("c:\\sam.bat")
 
import subprocess
'''
cmd = 'cmd.exe c:\\miners\0.1.0b\sam.bat'
p = subprocess.Popen("cmd.exe /c" + r"c:\\miners\0.1.0b\sam.bat abc", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
curline = p.stdout.readline()
while(curline != b''):
    print(curline)
    curline = p.stdout.readline()
     
p.wait()
print(p.returncode)
'''
cmd = 'miner.exe c:\\miners\0.1.0b\f2pool.bat'
p = subprocess.Popen("miner.exe /c" + r"c:\\miners\0.1.0b\f2pool.bat", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
curline = p.stdout.readline()
while(curline != b''):
    print(curline)
    curline = p.stdout.readline()
     
p.wait()
print(p.returncode)