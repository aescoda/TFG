#!/usr/bin/env python
# -*- coding: utf-8 -*-
from suds.client import Client
from suds.wsse import Security,UsernameToken

def get_email(iccid):

    wsdlurl= "http://apitest.jasperwireless.com/ws/schema/Terminal.wsdl"
    username="aescodaAPI"
    password= "!1994Whor5qp"
    license_key= "7c41495d-5047-4d2c-b01c-e5cb91ce6756"
    #disable certificate verification
    
    print("***** create the SOAP client")
    clientService = Client(wsdlurl)

    print("***** compose the SOAP security header")
    # add WSSE
    security = Security()
    token = UsernameToken(username, password)
    security.tokens.append(token)
    clientService.set_options(wsse=security)

    print("***** compose the SOAP body")
    #define imsi as a complext type
    #We compose the SOAP body for the EditTerminalRequest with the accountid we get from the previous function

    EditTerminalRequest = dict(messageId="1001", version="1.0", licenseKey=license_key, iccid=iccid, targetValue="DEACTIVATED_NAME", changeType="3")

    #We send to Jasper our SOAP request with the function in the WSDL file EditTerminal and get the response in a variable
    EditTerminalResponse = clientService.service.EditTerminal(**EditTerminalRequest)
    print EditTerminalResponse
    #As this PULL request is for deactivate the SIM we return None
    return None
iccid = "80191104961342800866"
get_email(iccid)
