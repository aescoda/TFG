    #!/usr/bin/env python
    # -*- coding: utf-8 -*-


from flask import Flask
import emailing

# Flask app should start in global layout
app = Flask(__name__)

@app.route('\webhook', methods=['POST','GET'])
def webhook:
   mail_cheking();
   return none

if __name__ == '__main__':
    app.run()
    
    
