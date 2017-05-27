    #!/usr/bin/env python
    # -*- coding: utf-8 -*-


from flask import Flask
import Emailing
import os

# Flask app should start in global layout
app = Flask(__name__)

@app.route('\webhook', methods=['POST','GET'])
def webhook():
    mail_cheking();
    return none

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port, host='0.0.0.0', threaded=True)
    
    
