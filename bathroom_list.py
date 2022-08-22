from settings import ALL
from threading import Timer
from datetime import datetime
from emails import send_alert
import csv
import os

timestamps = {}

def timer(student_id):
	send_alert(student_id, len(timestamps))

def register_id(student_id):
	if student_id not in timestamps:
		timestamps[student_id] = datetime.now()
		t = Timer(ALL["ALERT_THRESHOLD"]*60, lambda: timer(student_id))
		t.start()

		return 'register'

	else:
		start_time = timestamps[student_id]
		end_time = datetime.now()
		
		duration = end_time-start_time
		duration_in_m = str(round(duration.total_seconds()/60, 2))

		del timestamps[student_id]
		
		with open(ALL["LOG_PATH"], "a") as file:
			writer = csv.writer(file)
			writer.writerow([student_id, start_time.strftime("%m/%d/%Y %H:%M:%S"), end_time.strftime("%m/%d/%Y %H:%M:%S"), duration_in_m])

		return 'unregister'	

def create_logs():
	if not os.path.isfile(ALL["LOG_PATH"]):
		with open(ALL["LOG_PATH"], 'w') as file:
			writer = csv.writer(file)
			writer.writerow(["Student ID", "Leave Time", "Return Time", "Duration (minutes)"])

