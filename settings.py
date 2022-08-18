import os, sys
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

RECV_EMAIL = os.environ.get("RECV_EMAIL")
SEND_EMAIL = os.environ.get("SEND_EMAIL")
EMAIL_PASSWD = os.environ.get("EMAIL_PASSWD")
ALERT_THRESHOLD = int(os.environ.get("ALERT_THRESHOLD"))
LOG_PATH = os.environ.get("LOG_PATH")
TEACHER_NAME = os.environ.get("TEACHER_NAME")

def update(new):
	global RECV_EMAIL, SEND_EMAIL, EMAIL_PASSWD, ALERT_THRESHOLD, LOG_PATH, TEACHER_NAME

	try:
		with open(dotenv_path, 'w') as file:
			TEMPLATE = f'''
RECV_EMAIL="{new["RECV_EMAIL"]}"
SEND_EMAIL="{new["SEND_EMAIL"]}"
EMAIL_PASSWD="{new["EMAIL_PASSWD"]}"
TEACHER_NAME="{new["TEACHER_NAME"]}"
ALERT_THRESHOLD={new["ALERT_THRESHOLD"]} # minutes
LOG_PATH="{new["LOG_PATH"]}"
FLASK_APP="backend.py"
FLASK_DEBUG=1
				'''

			file.write(TEMPLATE)
	except: 
		return "failure"	

	load_dotenv(dotenv_path)

	RECV_EMAIL = os.environ.get("RECV_EMAIL")
	SEND_EMAIL = os.environ.get("SEND_EMAIL")
	EMAIL_PASSWD = os.environ.get("EMAIL_PASSWD")
	ALERT_THRESHOLD = int(os.environ.get("ALERT_THRESHOLD"))
	LOG_PATH = os.environ.get("LOG_PATH")
	TEACHER_NAME = os.environ.get("TEACHER_NAME")

	return 'success'