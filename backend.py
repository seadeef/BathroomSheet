import os
from bathroom_list import register_id
from flask import Flask, render_template, request, redirect, flash, get_flashed_messages
from uuid import uuid4
from settings import ALERT_THRESHOLD, EMAIL_PASSWD, SEND_EMAIL, RECV_EMAIL, TEACHER_NAME, LOG_PATH, update

app = Flask(__name__)
app.secret_key = uuid4().hex

@app.route('/', methods=['GET'])
def index():
    status = get_flashed_messages()

    if len(status) == 0:
        status = ['none']

    return render_template('index.html', status=status[0], alert_threshold=ALERT_THRESHOLD, teacher_name=TEACHER_NAME)

@app.route('/admin')
def admin():

    status = get_flashed_messages()

    if len(status) == 0:
        return redirect("/admin-auth")

    if status[0] != "is-auth=true":
        return redirect("/admin-auth")

    all_data = [
        {"name": "ALERT_THRESHOLD", "value": ALERT_THRESHOLD},
        {"name": "EMAIL_PASSWD", "value": EMAIL_PASSWD},
        {"name": "SEND_EMAIL", "value": SEND_EMAIL},
        {"name": "RECV_EMAIL", "value": RECV_EMAIL},
        {"name": "TEACHER_NAME", "value": TEACHER_NAME},
        {"name": "LOG_PATH", "value": LOG_PATH}
    ]

    return render_template('admin.html', data=all_data)

@app.route('/admin-auth')
def admin_auth():
    status = get_flashed_messages()

    if len(status) == 0:
        status = ['none']

    return render_template('admin-auth.html', status=status[0], teacher_name=TEACHER_NAME)

@app.route('/api/update-settings', methods=['POST'])
def update_settings():
    status = update({
        "RECV_EMAIL": request.form.get("RECV_EMAIL"),
        "SEND_EMAIL": request.form.get("SEND_EMAIL"),
        "ALERT_THRESHOLD": int(request.form.get("ALERT_THRESHOLD")),
        "EMAIL_PASSWD": request.form.get("EMAIL_PASSWD"),
        "TEACHER_NAME": request.form.get("TEACHER_NAME"),
        "LOG_PATH": request.form.get("LOG_PATH")
    })

    flash(f'update-settings-{status}')
    return redirect('/')

@app.route('/api/admin-auth', methods=['POST'])
def check_password():
    if request.form.get('password') == EMAIL_PASSWD:
        flash('is-auth=true')
        return redirect('/admin')
    else:
        flash('password-failure')
        return redirect('/admin-auth')

@app.route('/api/student-ids', methods = ['POST'])
def student_ids():
    status = register_id(request.form.get('student_ID'))
    flash(status)
    return redirect("/")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
