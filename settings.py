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
		new_recv_email = new["RECV_EMAIL"] if new["RECV_EMAIL"] else ALL["RECV_EMAIL"]
		new_send_email = new["SEND_EMAIL"] if new["SEND_EMAIL"] else ALL["SEND_EMAIL"]
		new_email_passwd = new["EMAIL_PASSWD"] if new["EMAIL_PASSWD"] else ALL["EMAIL_PASSWD"]
		new_admin_passwd = new["ADMIN_PASSWD"] if new["ADMIN_PASSWD"] else ALL["ADMIN_PASSWD"]
		new_teacher_name = new["TEACHER_NAME"] if new["TEACHER_NAME"] else ALL["TEACHER_NAME"]
		new_alert_threshold = int(new["ALERT_THRESHOLD"] if new["ALERT_THRESHOLD"] else ALL["ALERT_THRESHOLD"])
		new_log_path = new["LOG_PATH"] if new["LOG_PATH"] else ALL["LOG_PATH"]

		with open(dotenv_path, 'w') as file:
			TEMPLATE = f'''
RECV_EMAIL="{escape(new_recv_email, quote=True)}"
SEND_EMAIL="{escape(new_send_email, quote=True)}"
EMAIL_PASSWD="{escape(new_email_passwd, quote=True)}"
ADMIN_PASSWD="{escape(new_admin_passwd, quote=True)}"
TEACHER_NAME="{escape(new_teacher_name, quote=True)}"
ALERT_THRESHOLD={new_alert_threshold} # minutes
LOG_PATH="{escape(new_log_path, quote=True)}
FLASK_APP="backend.py"
FLASK_DEBUG=1
			'''

			file.write(TEMPLATE)
			
			## The above code just rewrites the .env file, for next time
	except Exception as e: 
		print(e)
		return "failure"	

	# Update each value in the dictionary 
	ALL["RECV_EMAIL"] = new_recv_email
	ALL["SEND_EMAIL"] = new_send_email
	ALL["EMAIL_PASSWD"] = new_email_passwd
	ALL["ADMIN_PASSWD"] = new_admin_passwd
	ALL["TEACHER_NAME"] = new_teacher_name
	ALL["ALERT_THRESHOLD"] = new_alert_threshold
	ALL["LOG_PATH"] = new_log_path

	return 'success'