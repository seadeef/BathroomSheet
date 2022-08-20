import smtplib, ssl
from settings import ALL

port = 465  # For SSL

# Create a secure SSL context
context = ssl.create_default_context()

def send_alert(student_id, num_students):
	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
		if ALL["ALERT_THRESHOLD"] == 1:
			words = ["Minute"]
		else:
			words = ["Minutes"]

		if num_students == 1:
			words.extend(["is", "student"])
		else:
			words.extend(["are", "students"])

		teacher = ALL["TEACHER_NAME"]
		alert = ALL["ALERT_THRESHOLD"]
		message = f"{teacher}'s Bathroom Pass System:\nSubject: Student {student_id} Has Been Gone for At Least {alert} {words[0]}!\nThere {words[1]} currently {num_students} {words[2]} on a bathroom break. Please take action to ensure the attendance of any missing students."
		server.login(ALL["SEND_EMAIL"], ALL["EMAIL_PASSWD"])
		server.sendmail(ALL["SEND_EMAIL"], ALL["RECV_EMAIL"], message)
