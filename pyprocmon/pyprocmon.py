#!/usr/bin/env python
'''
Created on July 24 2014

@author: shireenrao
'''

import os
import time
import sys
import subprocess


def checkprocess(owner, *args):
    ''' look at system processes and check if given process is running '''
    found = False
    proc_name,ident = args
    ps = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE,)
    user = subprocess.Popen(['grep', owner],
                            stdin=ps.stdout,
                            stdout=subprocess.PIPE,)
    process = subprocess.Popen(['grep', proc_name],
                            stdin=user.stdout,
                            stdout=subprocess.PIPE,)
    all_procs = process.stdout
    for proc_line in all_procs:
        if ident in proc_line and 'pyprocmon.py' not in proc_line:
            print 'proc_line ', proc_line
            found = True
            break

    return found

if len(sys.argv) < 2:
    print "Usage: %s scriptname [args]" % (sys.argv[0])
    sys.exit(1)

proc_to_monitor = sys.argv[1]
print "Process to monitor: " + proc_to_monitor
the_cmd = sys.argv[1:]
print "Run this to start process: " + " ".join(the_cmd)
run_mins = 50

num_secs_to_run = run_mins*60
start_time = time.time()
end_time = start_time + num_secs_to_run
#while time.time() < end_time:
check = checkprocess('shireenrao', proc_to_monitor, 'Python')
if check:
    print "Process is running"
else:
    print "Process is not running"
