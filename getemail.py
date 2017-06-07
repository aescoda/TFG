# -*- coding: utf-8 -*-
import logging
import ssl
from suds.client import Client
from suds.wsse import Security,UsernameToken

def get_email(iccid):


    service='terminal'#??
    wsdlurl= os.environ.get('WSDL_FILE', None)
    username= os.environ.get('USER_NAME', None)
    password= os.environ.get('USER_PASS', None)
    license_key= os.environ.get('LICENSE_KEY', None)


    print("***** create the SOAP client")
    clientService = Client(wsdlurl)
    print clientService

    print("***** compose the SOAP security header")
    # add WSSE
    security = Security()
    token = UsernameToken(username, password)
    security.tokens.append(token)
    clientService.set_options(wsse=security)

    print("***** compose the SOAP body")
    #define imsi as a complext type
    iccid = "89302720396916796910"
    getTerminalsDetailsRequest = dict(messageId="1001", version="1.0", licenseKey=license_key, iccid=iccid)

    print("***** SOAP request is:")
    print getTerminalsDetailsRequest

    getTerminalsDetailsResponse = clientService.service.GetTerminalsDetails(**getTerminalsDetailsRequest)

    print("***** SOAP response is:")
    print(getTerminalsByImsiResponse)
    iccid = (getTerminalsDetailsResponse.terminals.terminal[0].accountId)
    print(iccid)
