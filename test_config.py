import os

# Change this to change the environment from dev to production (non-testing)
TESTING = True

SECRET_KEY = 'Z6nP3q9U1zo7rvS'

UPLOAD_FOLDER = '/home/ubuntu/workspace/uploads'
LOG_FILE = 'logs.txt'

G_CAPTCHA_VERIFY = 'https://www.google.com/recaptcha/api/siteverify'
G_CAPTCHA_SITEKEY = '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI'
G_CAPTCHA_SECRET = '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'

FIREBASE_AUTH_FILE = 'config/fb-admin-key.json'
FIREBASE_USER_NAME = os.environ.get('FIREBASE_USER_NAME', '')
FIREBASE_USER_PWD = os.environ.get('FIREBASE_USER_PWD', '')

API_KEY = 'LXotJB66d3Qm8NP'

UPLOADED_CSVS_DEST = '/home/ubuntu/workspace/uploads'