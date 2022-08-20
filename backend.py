import os
from bathroom_list import register_id
from flask import Flask, render_template, request, redirect, flash, get_flashed_messages
from uuid import uuid4
from settings import ALL, update

app = Flask(__name__)
app.secret_key = uuid4().hex

@app.route('/', methods=['GET'])
def index():
    status = get_flashed_messages()

    if len(status) == 0: # If there are not any updates, then tell Jinja to not render any message
        status = ['none']

	# Render
    return render_template('index.html', status=status[0], alert_threshold=ALL["ALERT_THRESHOLD"], teacher_name=ALL["TEACHER_NAME"])

@app.route('/admin')
def admin():
    status = get_flashed_messages()

    if len(status) == 0: # If this page is just being accessed directly, reroute to the auth page
        return redirect("/admin-auth")

    if status[0] != "is-auth=true": # If the flash is wrong
        return redirect("/admin-auth")

    all_data = map(lambda x: {"name": x, "value": ALL[x]}, ALL) # Map data into parseable format

    return render_template('admin.html', data=all_data)

@app.route('/admin-auth')
def admin_auth():
    status = get_flashed_messages()

    if len(status) == 0: # If there are no flashed messages, then tell Jinja not to render any message
        status = ['none']

    return render_template('admin-auth.html', status=status[0], teacher_name=ALL["TEACHER_NAME"])

@app.route('/api/update-settings', methods=['POST'])
def update_settings():
	# Update the settings 
    status = update({
        "RECV_EMAIL": request.form.get("RECV_EMAIL"),
        "SEND_EMAIL": request.form.get("SEND_EMAIL"),
        "ALERT_THRESHOLD": int(request.form.get("ALERT_THRESHOLD")),
        "EMAIL_PASSWD": request.form.get("EMAIL_PASSWD"),
        "ADMIN_PASSWD": request.form.get("ADMIN_PASSWD"),
        "TEACHER_NAME": request.form.get("TEACHER_NAME"),
        "LOG_PATH": request.form.get("LOG_PATH"),
    })

    flash(f'update-settings-{status}')
    return redirect('/')

## API Routes ##

@app.route('/api/admin-auth', methods=['POST'])
def check_password():
	# If the passord is correct, send the "correct" message
    if request.form.get('password') == ALL["ADMIN_PASSWD"]:
        flash('is-auth=true')
        return redirect('/admin')
    else: # Send the fail message
        flash('password-failure')
        return redirect('/admin-auth')

@app.route('/api/student-ids', methods = ['POST'])
def student_ids():
    status = register_id(request.form.get('student_ID')) # Register a student to the bathroom, and say that
    flash(status)
    return redirect("/")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
