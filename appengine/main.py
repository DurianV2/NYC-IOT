# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START app]
import logging

# [START imports]
from flask import Flask, render_template, request
from dateutil import parser
from json import dumps
# [END imports]

# [START create_app]
app = Flask(__name__)
# [END create_app]

# [Start app variables]
estimated_date_time_of_arrival = None
owner_is_home = False
send_first_alert = False

# [End app variables]

def update_eta(eta):
    estimated_data_time_of_arrival = parser.parse(eta)

# [START leaving]
@app.route('/leaving')
def leavingform():
    return render_template('leavingform.html')
# [END leaving]

# [START update]
@app.route('/update')
def updateform():
    return render_template('updateform.html')
# [END update]

def submitted_form():
    name = request.form['name']
    email = request.form['email']
    site = request.form['site_url']
    comments = request.form['comments']

# [START submittedleaving]
@app.route('/submittedleaving', methods=['POST'])
def submitted_leaving():
    ETA = request.form['ETA']
    phone1 = request.form['phone1']
    phone2 = request.form['phone2']
    phone3 = request.form['phone3']
    phone4 = request.form['phone4']
    phone5 = request.form['phone5']
    update_eta(ETA)

    # [END submittedleaving]
    # [START render_template]
    return render_template('submitted_form.html')
    # [END render_template]

# [START submitted]
@app.route('/submittedupdate', methods=['POST'])
def submitted_update():
    ETA = request.form['ETA']
    update_eta(ETA)
    # TODO(innocent) Add logic to check the status of this button after it has been created.

    # [END submitted]
    # [START render_template]
    return render_template('submitted_form.html')
    # [END render_template]

@app.route('/sync' methods=['GET'])
def sync():
    sync_message = {
        'is_home': owner_is_home,
        'send_alert': send_first_alert
    }
    return dumps(sync_message)

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]
