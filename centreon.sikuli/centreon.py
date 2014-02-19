from sikuli import *
import sys
import time
import logging

Settings.ActionLogs = False
Settings.InfoLogs = False
Settings.DebugLogs = False

warning = sys.argv[2]
critical = sys.argv[3]
log_file = sys.argv[4]

fmt = "%(message)s"
logging.basicConfig(filename=log_file, filemode='a', format=fmt, level=logging.INFO)
logging.info("<h1>%s</h1>" %(sys.argv[0]))
logging.info("<ul>")
logging.info("<li>Date: " + time.strftime('%d/%m/%y %H:%M:%S', time.localtime()) + "</li>")

def status(exit_code, diff_time, desc='none'):
	time_code = getTimeCode(diff_time)
	logging.info("<li>Warning treshold: %ss</li>" %(warning))
	logging.info("<li>Critical treshold: %ss</li>" %(critical))
	logging.info("<li>execution time: %.1fs</li>" %(diff_time))
	logging.info("<li>time code: %s</li>" %(getStatus(time_code)))

	if exit_code == 0:
		if time_code == 1:
			exit_code = 1
		elif time_code == 2:
			exit_code = 2

	logging.info("<li>error: %s</li>" %(desc))
	logging.info("<li>exit code: %s</li>" %(getStatus(exit_code)))
	logging.info("</ul>")

	output = "CHECKRDP %s - Execution time = %.1fs | time=%.1fs;%s;%s" %(getStatus(exit_code), diff_time, diff_time, warning, critical)
	output += "\nError: %s" %(desc)
        sys.stderr.write(output) #check_sikuli swaps stderr and stdin

	#sys.exit(exit_code)
	exit(exit_code)

def getTimeCode(diff_time):
	if diff_time < float(warning):
		return 0
	elif diff_time < float(critical):
		return 1
	elif diff_time >= float(critical):
		return 2

def getStatus(code):
	if code == 0:
		return "OK"
	elif code == 1:
		return "WARNING"
	elif code == 2:
		return "CRITICAL"
