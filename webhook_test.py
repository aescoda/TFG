    #!/usr/bin/env python
    # -*- coding: utf-8 -*-


from flask import Flask
import os
import Emailing

# Flask app should start in global layout
app = Flask(__name__)

@app.route("/webhook", methods=['POST','GET'])
def webhook():
    test = email_checking();
    return None

if __name__ == "__main__":
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port, host='0.0.0.0', threaded=True)
    
    
