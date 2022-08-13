from bathroom_list import register_id
from flask import Flask, send_from_directory, request, redirect
import os 

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory(os.path.join(".", "static"), "index.html")

@app.route('/studentids', methods = ['POST'])
def student_ids():
    register_id(request.form.get('student_ID'))
    return redirect("/")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
