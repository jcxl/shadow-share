"""ShadowShare Server Backend
"""
from flask import Flask

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['DB_PATH'] = 'server/enigshare.db'
app.debug = True

import server.views
import server.io