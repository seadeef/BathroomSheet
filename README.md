# BathroomSheet
A digital bathroom pass system written in Flask and designed with Bootstrap.

## Features
* Email alerts of extended absences 
* Detailed logs of every bathroom trip
* Integrated configuration panel and admin authentication
* Simple interface for students
## Installation

First, clone the repository to your local filesystem and navigate to the created directory.
```bash
git clone https://github.com/seadeef/BathroomSheet.git && cd BathroomSheet/
```
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the needed packages.

```bash
pip3 install -r requirements.txt
```

## Usage
Every time you want to start the app, run the following command:
```bash
python3 backend.py
```
A development server should now be running on all interfaces at port `5000`. To navigate to the page locally, enter `http://127.0.0.1:5000` into your browser. 

## Configuration
The default admin password is `soap`. After setting up the server, the first thing you should do is navigate to the admin panel (a link is found at the footer of the index page) and log in with the default password. Then, make sure you change the password to something you will remember, and configure all other settings as appropriate. In order to receive email alerts, you need to create a gmail account with [less secure apps access](https://myaccount.google.com/lesssecureapps) **turned ON**. Make sure to enter the receiving email address into the `RECV_EMAIL` field, the sending address into the `SEND_EMAIL` field, and the password of the sending address into the `EMAIL_PASSWD` field. Configuration options also available are `TEACHER_NAME`, which changes how your name is displayed on various pages; `LOG_PATH`, which changes where logs are written to; and `ALERT_THRESHOLD`, the number of minutes that have to pass before receiving an email alert of a student absence.

## Credits
Coded by Kevin Toren and Gautam Khajuria. Requested by Mr. Turner.
