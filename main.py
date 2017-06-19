#!/usr/bin/env python
# -*- coding: utf-8 -*-

#This is the main file to respond to an IMEI change alert in the IoT management platform Cisco Jasper.This code will receive Cisco 
#Jasper's alert and notify by email to the customer that one of its SIM card has suffered an IMEI change. If the IMEI change is 
#intentional the customer will ignore the email, if it is not, the customer is suffering an attack and will have the possibility
#of getting the location of the SIM card and deactivate it with the link in the email received.

# Note that this time the following code has been divided in different files
# to make a clearer code.

# Disclaimer: Don´t use this code as a best practices example, as it has not
# been verified as the best way of coding Python. Refer to
# https://www.python.org/ for reliable documentation.


from flask import Flask
from flask import request
import xml.etree.ElementTree as ET
from threading import Thread
import geocoder

#Private libraries create for the app development
import email_lib
import jasper_lib


#We use a Flask app as a global layout
app = Flask(__name__)

#We declare this variables as global so we can use it in both webhooks
iccid = ""
admin_details = 
customer_email =""
event = ""
xml = ""

#We define a thread that will run after receiving the notification from Jasper into the /webhook listener. We need to create this
#thread as Jasper will resend the notification unless it receives a 'status 200' HTTPS message
def send_email(xml):
    #We mark this variables as global so the assigments done to them in this threat will affect variable used in the /response webhook
    global iccid
    global customer_email
    global admin_details
    global event
    global xml
    #Here we parse the data receive as a unicode into a elementtree object to process it as XML file and get the iccid affected
    event = req['eventType']
    data = req['data'] 
    xml = ET.fromstring(xml)
    iccid = req[0]
    #All the details needed for the first email notification will be obteined through these functions
    admin_details = jasper_lib.Terminals.get_account(iccid)
    customer_email = jasper_lib.Accounts.get_email(admin_details)
    #We create and send an email to the customer affected depending on the alert 
    email_lib.email_alert(customer_email, iccid,event)
    return None
    

#Jasper alerts will be sent receive in this webhook.
@app.route('/alert', methods=['POST','GET'])
def alert():
    #We will extract the body of the HTTPS POST to use it for the application communications
    req = request.form
    #We open a new thread to process the data received as we need to answer Jasper to stop receiving messages
    t = Thread(target=send_email, args=(req,))
    t.start()
    #Jasper will resend the notification unless it receives a status 200 confirming the reception
    return '',200
    
#If we are facing a real unauthorized IMEI change we will receive the confirmation from the customer in this webhook.
@app.route('/response', methods=['POST','GET'])
def response:
    if event == "SIM_STATE_CHANGE":
    #We change the status of the SIM to activated again
    jasper_lib.Terminals.reactivateSIM(iccid)
    data = iccid
    elif event == "IMEI_CHANGE":
    #We get the location of the SIM card with the Jasper function
    location = jasper_lib.Terminals.get_location(iccid)
    #We deactivate the SIM card as we already have the location
    jasper_lib.Terminals.deactivateSIM(iccid)
    #We find the exact location of the SIM with a library created by google to get location information in JSON
    address = geocoder.google(location, method='reverse')
    #We pack the data in an array to use it in the email
    data = (location[0],location[1],iccid,address)
    elif event == "DATA_LIMIT":
    #We get the usage of the iccid  
    usage = jasper_lib.Billing.get_usage(iccid)
    data = usage
    elif event == "CTD_SESSION_USAGE_EXCEEDED":
    #As we won't take action after the first email we don't need a second answer 
    data = ""  
    #We send an email to the customer with the location of the SIM card    
    email_lib.email_action(customer_email,data)
    return "Acabamos de procesar su petición, en breve recibirá un email con los detalles"
    
# App is listening to webhooks. Next line is used to executed code only if it is
# running as a script, and not as a module of another script.
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port, host='0.0.0.0', threaded=True)
