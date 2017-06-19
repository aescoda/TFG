#!/usr/bin/env python
# -*- coding: utf-8 -*-

##This file contains all the functions to interact with Cisco Jasper and get the information related with the SIM card affected in the 
#main.py file. This communication will be done using SOAP protocol and a license key provided through Jasper

import os
from suds.client import Client
from suds.wsse import Security,UsernameToken

#For security reasons we storage all the private information in Heroku server as system variables. We will read them for makeing 
#the conection with Cisco Jasper 

class Terminals():
    def __init__(self):
        wsdlurl= os.environ.get('WSDL_FILE', None)
        username= os.environ.get('USER_NAME', None)
        password= os.environ.get('USER_PASS', None)
        self.license_key= os.environ.get('LICENSE_KEY', None)

        #We need to create a SOAP client to make a communication with Cisco Jasper API server using the wsdlurl file that contains the functions
        self.clientService = Client(wsdlurl)

        #We add a security header to the SOAP messages for web services with the username and password for the Jasper Control Center
        security = Security()
        token = UsernameToken(username, password)
        security.tokens.append(token)
        (self.clientService).set_options(wsse=security)
    
    ##This are all the funcionts that we use to communicate with Jasper and get the values of the SIM affected
    def get_account(iccid):
        #We compose the SOAP body for the getTerminalDetailsRequest with the iccid we want the details from as a dictionary  
        iccid = dict(iccid=iccid)
        getTerminalsDetailsRequest = dict(messageId="1001", version="1.0", licenseKey=self.license_key, iccids=iccid)

        #We send to Jasper our SOAP request with the function in the WSDL file GetTerminalDetails and get the response in a variable
        getTerminalsDetailsResponse = (self.clientService).service.GetTerminalDetails(**getTerminalsDetailsRequest)

        #We parse the SOAP response to find the values we need of the SIM card and return them
        accountid = (getTerminalsDetailsResponse.terminals.terminal[0].accountId)
        return accountid
      
    def deactivate_SIM(iccid):
        #We compose the SOAP body for the EditTerminalRequest with the accountid we get from the previous function
        EditTerminalRequest = dict(messageId="1001", version="1.0", licenseKey=self.license_key, iccid=iccid, targetValue="DEACTIVATED_NAME", changeType="3")
        #We send to Jasper our SOAP request with the function in the WSDL file EditTerminal and get the response in a variable    
        EditTerminalResponse = (self.clientService).service.EditTerminalDetails(**EditTerminalRequest)
        #As this PULL request is for deactivate the SIM we return None
        return None
    
    def reactivate_SIM(iccid):
        #We compose the SOAP body for the EditTerminalRequest with the accountid we get from the previous function
        EditTerminalRequest = dict(messageId="1001", version="1.0", licenseKey=self.license_key, iccid=iccid, targetValue="ACTIVATED_NAME", changeType="3")
        #We send to Jasper our SOAP request with the function in the WSDL file EditTerminal and get the response in a variable    
        EditTerminalResponse = (self.clientService).service.EditTerminalDetails(**EditTerminalRequest)
        #As this PULL request is for deactivate the SIM we return None
        return None

    def get_location(iccid):
        #We compose the SOAP body for the GetLocationRequest with the accountid we get from the previous function
        getLocationRequest = dict(messageId="1001", version="1.0", licenseKey=self.license_key, iccid=iccid)

        #We send to Jasper our SOAP request with the function in the WSDL file GetTerminalDetails and get the response in a variable
        getLocationResponse = (self.clientService).service.GetLocation(**getLocationRequest)

        #We parse the SOAP response to find the value we need of the SIM card and return it
        longitude = getLocationResponse.terminals.location.longitude
        latitude = getLocationResponse.terminals.location.latitude
        #This function has been implemented by a 3rd party company and it is only for its use. For continue the developing of the project  
        #we will simulate the coordinates of the SIM card.  
        return longitude, latitude
                        

class Accounts:
    def __init__(self):
        wsdlurl= os.environ.get('WSDL_FILE2', None)
        username= os.environ.get('USER_NAME', None)
        password= os.environ.get('USER_PASS', None)
        self.license_key= os.environ.get('LICENSE_KEY', None)

        #We need to create a SOAP client to make a communication with Cisco Jasper API server using the wsdlurl file that contains the functions
        self.clientService = Client(wsdlurl)

        #We add a security header to the SOAP messages for web services with the username and password for the Jasper Control Center
        security = Security()
        token = UsernameToken(username, password)
        security.tokens.append(token)
        (self.clientService).set_options(wsse=security)                
     
    def get_email (accountid):
        #We compose the SOAP body for the getAccountDetailsRequest with the accountid we get from the previous function
        accountid = dict(accountid = accountid)
        getAccountDetailsRequest = dict(messageId="1001", version="1.0", licenseKey=self.license_key, accountids=accountid)

        #We send to Jasper our SOAP request with the function in the WSDL file GetTerminalDetails and get the response in a variable
        getAccountDetailsResponse = (self.clientService).service.GetAccountDetails(**getAccountDetailsRequest)

        #We parse the SOAP response to find the value we need of the SIM card and return it
        email = getAccountDetailsResponse.accounts.account.billing.contact.email
        return email
                     
                    
class Billing():
    def __init__(self):
        wsdlurl= os.environ.get('WSDL_FILE3', None)
        username= os.environ.get('USER_NAME', None)
        password= os.environ.get('USER_PASS', None)
        self.license_key= os.environ.get('LICENSE_KEY', None)

        #We need to create a SOAP client to make a communication with Cisco Jasper API server using the wsdlurl file that contains the functions
        self.clientService = Client(wsdlurl)

        #We add a security header to the SOAP messages for web services with the username and password for the Jasper Control Center
        security = Security()
        token = UsernameToken(username, password)
        security.tokens.append(token)
        (self.clientService).set_options(wsse=security)

    def get_usage(iccid):
        #We compose the SOAP body for the getAccountDetailsRequest with the accountid we get from the previous function
        getUsageRequest = dict(messageId="1001", version="1.0", licenseKey=self.license_key, iccid=iccid)

        #We send to Jasper our SOAP request with the function in the WSDL file GetTerminalDetails and get the response in a variable
        getUsageResponse = (self.clientService).service.GetTerminalUsage(**getUsageRequest)

        #We parse the SOAP response to find the value we need of the SIM card and return it
        data_volume = getUsageResponse.totalDataVolume
        start_date = getUsageResponse.cycleStartDate
        SMS_volume = getUsageResponse.totalSMSVolume
        Voice_volume = getUsageResponse.totalVoiceVolume            
        return data_volume, start_date, SMS_volume, Voice_volume
          
