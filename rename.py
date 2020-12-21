import os
import subprocess

dir = 'C:/Users/may/Music/audiobooks/the dragon republic/'
os.chdir(dir)

for p,d,f in os.walk(dir):
    for fn in f:
        new_fn = fn.replace('y2mate.com - ', '')
        fn = '\"' + fn + '\"'
        new_fn = '\"' + new_fn + '\"'
        cmdln = 'ren ' + fn + ' ' + new_fn
        print(cmdln)
        subprocess.call(cmdln, shell=True)

