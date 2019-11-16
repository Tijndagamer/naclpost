#!/usr/bin/python3
"""
    app.py
    This file is part of naclpost.

    Copyright (c) 2019 Martijn

    naclpost is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    naclpost is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with naclpost.  If not, see <http://www.gnu.org/licenses/>.
"""

from flask import Flask
from flask import abort
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask import flash
from flask import json

from werkzeug.utils import secure_filename

import os
import uuid
from random import randint

UPLOAD_FOLDER = "/tmp/nacluploads"
ALLOWED_EXTENSIONS =set(["txt"])

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if os.path.isdir(app.config["UPLOAD_FOLDER"]) is False:
    print("UPLOAD_FOLDER does not exist yet, creating...")
    os.mkdir(app.config["UPLOAD_FOLDER"])


#
# URL Handlers
#

@app.route("/")
def index_page():
    return render_template("index.html")


#
# Error handlers
#

@app.errorhandler(404)
def err_page_not_found(error):
    return render_template("404.html"), 404
