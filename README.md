PyProcMon
=========

My lame attempt at a process monitor.

filewatcher is a script to demonstrate a long running process. PyProcMon is a
program which is used to monitor your long running process. It wakes up every 5
minutes to check if the long running process is running or not. If it is not,
it will start up the process. If it is running it will got to sleep for 5
minutes.

TODO: I need the ability to log the long running process. I know I can achieve
this using the logging module to log to a file. I need to find out if I can do
this any other way.
