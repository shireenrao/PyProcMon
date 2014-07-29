#!/usr/bin/env python
'''
Created on July 23 2014

@author shireenrao
'''


import errno
import os
import sys
import shutil
import time
from types import *


def create_dir_if_not_exist(path):
    """ Create the directory for given path if not exists """
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST:
            pass
        else:
            raise


def process(a_file):
    ''' process the file found '''
    parent_dir = os.path.dirname(os.path.dirname(a_file))
    backup_dir = os.path.join(parent_dir, 'backup')
    create_dir_if_not_exist(backup_dir)
    if os.path.isdir(backup_dir):
        try:
            shutil.move(os.path.abspath(a_file), backup_dir)
            print "%s moved to %s" % (a_file, backup_dir)
        except OSError as exc:
            if exc.errno == errno.EEXIST:
                pass
            else:
                pass


if len(sys.argv) < 3:
    print "Usage: %s [watchdir] [run_mins]" % sys.argv[0]
    sys.exit(1)

watchdir = sys.argv[1]
run_mins = int(sys.argv[2])

assert os.path.isdir(watchdir), "watchdir is not a valid directory: %s" % watchdir
assert type(run_mins) is IntType, "run_mins is not in minutes: %r" % run_mins

print "filewatcher will watch directory %s and will run for %s minutes" % (watchdir, str(run_mins))
num_secs_to_run = run_mins*60
start_time = time.time()
end_time = start_time + num_secs_to_run
while time.time() < end_time:
    print "Sleeping for 5 seconds"
    time.sleep(5)
    print "%r minutes left" % int((end_time - time.time())/60)
    try:
        print "Looking for files in %s" % watchdir
        file_dict = dict([(ffile, None) for ffile in os.listdir(watchdir)])
    except:
        print "Exception reading directory; retrying %s:%s" % (sys.exc_info()[0], sys.exc_info[1])
        time.sleep(60)
        file_dict = dict([(ffile, None) for ffile in os.listdir(watchdir)])

    if len(file_dict) > 0:
        print "Found %r files" % len(file_dict)
    else:
        print "Found 0 files"
    file_list = file_dict.keys()
    file_list.sort(reverse=True)
    for found_file in file_list:
        print "Begin processing file %s" % found_file
        file_full_path = os.path.join(watchdir, found_file)
        process(file_full_path)
        print "Processing complete"
