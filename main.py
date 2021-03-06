import os
import json
import requests
from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

SLACK_OUTGOING_WEBHOOK_TOKEN = os.environ.get('SLACK_OUTGOING_WEBHOOK_TOKEN', None)
SLACK_INCOMING_WEBHOOK_URL = os.environ['SLACK_INCOMING_WEBHOOK_URL']

@app.route('/webhook', methods=['POST'])
def webhook():
    token = request.form.get('token')
    if not SLACK_OUTGOING_WEBHOOK_TOKEN or token == SLACK_OUTGOING_WEBHOOK_TOKEN:
        params = {
                'username': 'anohippomous',
                'icon_emoji': ':anohippomous:',
                'text': request.form.get('text'),
                'channel': '#%s' % request.form.get('channel_name')
        }
        try:
            response = requests.post(SLACK_INCOMING_WEBHOOK_URL, data=json.dumps(params))
        except Exception as e:
            return 'Posting to Slack failed: %s' % str(e)
    return ''

