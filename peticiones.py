# -*- coding: utf-8 -*-
from suds.client import Client
from suds.wsse import Security,UsernameToken

def get_email(iccid):
    wsdlurl= "http://apitest.jasperwireless.com/ws/schema/Terminal.wsdl"
    username="aescodaAPI"
    password= "!1994Whor5qp"
    license_key= "7c41495d-5047-4d2c-b01c-e5cb91ce6756"
    #disable certificate verification
    #ssl._create_default_https_context = ssl._create_unverified_context

    #logging.basicConfig(level=logging.INFO)
    #logging.getLogger('suds.client').setLevel(logging.DEBUG)
    #logging.getLogger('suds.transport').setLevel(logging.DEBUG)
    #logging.getLogger('suds.suds.xsd.schema').setLevel(logging.DEBUG)
    #logging.getLogger('suds.wsdl').setLevel(logging.DEBUG)

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
    iccid = dict(iccid=iccid)
    getTerminalDetailsRequest = dict(messageId="123", version="1.0", licenseKey=license_key, iccids= iccid)

    print("***** SOAP request is:")


    getTerminalsDetailsResponse = clientService.service.GetTerminalDetails(**getTerminalDetailsRequest)
    print getTerminalsDetailsResponse

    print("***** SOAP response is:")
    #print(getTerminalsDetailsResponse)
    accountid = (getTerminalsDetailsResponse.terminals.terminal[0].accountId)
    print(accountid)
    return accountid
t = 0
if t = 0
a = get_email("80191104961342800866")
t = t+1
else
return ''
