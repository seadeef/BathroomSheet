import smtplib, ssl
from settings import RECV_EMAIL, SEND_EMAIL, EMAIL_PASSWD, ALERT_THRESHOLD

port = 465  # For SSL

# Create a secure SSL context
context = ssl.create_default_context()

def send_alert(student_id, num_students):
	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
		if ALERT_THRESHOLD == 1:
			words = ["Minute"]
		else:
			words = ["Minutes"]

		if num_students == 1:
			words.extend(["is", "student"])
		else:
			words.extend(["are", "students"])

		message = f"Subject: Student {student_id} Has Been Gone for {ALERT_THRESHOLD} {words[0]}!\nThere {words[1]} currently {num_students} {words[2]} on a bathroom break. Please take action to ensure the attendance of any missing students."
		server.login(SEND_EMAIL, EMAIL_PASSWD)
		server.sendmail(SEND_EMAIL, RECV_EMAIL, message)

