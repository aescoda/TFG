import json

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)

# Buffer for capturing messages from Jasper
sbuffer = {"sessionId":"","roomId":"","message":"",
           "personId":"","personEmail":"","displayName":""}
# Buffer for capturing messages from email
abuffer = {"sessionId":"","confident":"", "message":"","action":"",

# Message Received from Jasper
@app.route('/webhook', methods=['POST','GET'])
def webhook():
    
    #req = request.get_json(silent=True, force=True)
    #res = spark_webhook(req)
    print("FUNCIONA!")
    return None
