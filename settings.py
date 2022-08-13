import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

RECV_EMAIL = os.environ.get("RECV_EMAIL")
SEND_EMAIL = os.environ.get("SEND_EMAIL")
EMAIL_PASSWD = os.environ.get("EMAIL_PASSWD")
ALERT_THRESHOLD = int(os.environ.get("ALERT_THRESHOLD"))
LOG_PATH = os.environ.get("LOG_PATH")