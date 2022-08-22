from os import environ
from os.path import join, dirname, exists
from dotenv import load_dotenv
from html import escape, unescape

dotenv_path = join(dirname(__file__), '.env')

def create_settings():
	load_dotenv(dotenv_path)

	return {
		"RECV_EMAIL": unescape(environ.get("RECV_EMAIL")),
		"SEND_EMAIL": unescape(environ.get("SEND_EMAIL")),
		"EMAIL_PASSWD": unescape(environ.get("EMAIL_PASSWD")),
		"ADMIN_PASSWD": unescape(environ.get("ADMIN_PASSWD")),
		"TEACHER_NAME": unescape(environ.get("TEACHER_NAME")),
		"ALERT_THRESHOLD": int(environ.get("ALERT_THRESHOLD")),
		"LOG_PATH": unescape(environ.get("LOG_PATH"))
	}

if exists(join(dirname(__file__), '.env')):
	ALL = create_settings()

else:
	TEMPLATE = f'''
RECV_EMAIL="REPLACE_ME"
SEND_EMAIL="REPLACE_ME"
EMAIL_PASSWD="REPLACE_ME"
ADMIN_PASSWD="soap"
TEACHER_NAME="Teacher"
ALERT_THRESHOLD=10 # minutes
LOG_PATH="logs.txt"
FLASK_APP="backend.py"
FLASK_DEBUG=1
			'''
	with open(dotenv_path, 'w') as file:
		file.write(TEMPLATE)

	ALL = create_settings()



def update(new):
	# Make sure no errors seep through, just report them

	try:
		with open(dotenv_path, 'w') as file:
			escaped = escape(new["ALERT_THRESHOLD"] if new["ALERT_THRESHOLD"] else str(ALL["ALERT_THRESHOLD"]), quote=True) # fuck python this piece of shit language cant do basic parsing
			TEMPLATE = f'''
RECV_EMAIL="{escape(new["RECV_EMAIL"], quote=True)}"
SEND_EMAIL="{escape(new["SEND_EMAIL"], quote=True)}"
EMAIL_PASSWD="{escape(new["EMAIL_PASSWD"], quote=True)}"
ADMIN_PASSWD="{escape(new["ADMIN_PASSWD"], quote=True)}"
TEACHER_NAME="{escape(new["TEACHER_NAME"], quote=True)}"
ALERT_THRESHOLD={escaped} # minutes
LOG_PATH="{escape(new["LOG_PATH"], quote=True)}"
FLASK_APP="backend.py"
FLASK_DEBUG=1
			'''

			file.write(TEMPLATE)
			
			## The above code just rewrites the .env file, for next time
	except Exception as e: 
		print(e)
		return "failure"	

	# Update each value in the dictionary 
	ALL["RECV_EMAIL"] = new["RECV_EMAIL"]
	ALL["SEND_EMAIL"] = new["SEND_EMAIL"]
	ALL["EMAIL_PASSWD"] = new["EMAIL_PASSWD"]
	ALL["ADMIN_PASSWD"] = new["ADMIN_PASSWD"]
	ALL["TEACHER_NAME"] = new["TEACHER_NAME"]
	ALL["ALERT_THRESHOLD"] = str(new["ALERT_THRESHOLD"]) if new["ALERT_THRESHOLD"] else str(ALL["ALERT_THRESHOLD"])
	ALL["LOG_PATH"] = new["LOG_PATH"]

	return 'success'