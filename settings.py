import os, subprocess, platform
from os.path import join, dirname
import sys
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

## The use of these variables is highly discouraged, as they are not updated if Admin change it
RECV_EMAIL = os.environ.get("RECV_EMAIL")
SEND_EMAIL = os.environ.get("SEND_EMAIL")
EMAIL_PASSWD = os.environ.get("EMAIL_PASSWD")
ADMIN_PASSWD = os.environ.get("ADMIN_PASSWD")
ALERT_THRESHOLD = int(os.environ.get("ALERT_THRESHOLD"))
LOG_PATH = os.environ.get("LOG_PATH")
TEACHER_NAME = os.environ.get("TEACHER_NAME")

## On the other hand, this dictionary is updated if Admin changes it
ALL = {
	"RECV_EMAIL": RECV_EMAIL,
	"SEND_EMAIL": SEND_EMAIL,
	"EMAIL_PASSWD": EMAIL_PASSWD,
	"ADMIN_PASSWD": ADMIN_PASSWD,
	"TEACHER_NAME": TEACHER_NAME,
	"ALERT_THRESHOLD": ALERT_THRESHOLD,
	"LOG_PATH": LOG_PATH,
}

def update(new):
	global ALL

	# Make sure no errors seep through, just report them
	try:
		with open(dotenv_path, 'w') as file:
			TEMPLATE = f'''
RECV_EMAIL="{new["RECV_EMAIL"]}"
SEND_EMAIL="{new["SEND_EMAIL"]}"
EMAIL_PASSWD="{new["EMAIL_PASSWD"]}"
ADMIN_PASSWD="{new["ADMIN_PASSWD"]}"
TEACHER_NAME="{new["TEACHER_NAME"]}"
ALERT_THRESHOLD={new["ALERT_THRESHOLD"]} # minutes
LOG_PATH="{new["LOG_PATH"]}"
FLASK_APP="backend.py"
FLASK_DEBUG=1
				'''

			file.write(TEMPLATE)
			
			## The above code just rewrites the .env file, for next time
	except: 
		return "failure"	

	load_dotenv(dotenv_path) # Reload .env (this doesn't have an effect)

	# Update each value in the dictionary 
	ALL["RECV_EMAIL"] = new["RECV_EMAIL"]
	ALL["SEND_EMAIL"] = new["SEND_EMAIL"]
	ALL["EMAIL_PASSWD"] = new["EMAIL_PASSWD"]
	ALL["ADMIN_PASSWD"] = new["ADMIN_PASSWD"]
	ALL["TEACHER_NAME"] = new["TEACHER_NAME"]
	ALL["ALERT_THRESHOLD"] = new["ALERT_THRESHOLD"]
	ALL["LOG_PATH"] = new["LOG_PATH"]

	return 'success'