from flask import Flask
from flask import request
from flask import make_response
import os


app = Flask(__name__)

@app.route('/webhook', methods=['POST','GET'])
def webhook():
    print "Email1"
    return "holamundoa"

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port, host='0.0.0.0', threaded=True)
