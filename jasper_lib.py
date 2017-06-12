import os
from suds.client import Client
from suds.wsse import Security,UsernameToken


wsdlurl= os.environ.get('WSDL_FILE', None)
username= os.environ.get('USER_NAME', None)
password= os.environ.get('USER_PASS', None)
license_key= os.environ.get('LICENSE_KEY', None)


print("***** create the SOAP client")
clientService = Client(wsdlurl)


print("***** compose the SOAP security header")
# add WSSE
security = Security()
token = UsernameToken(username, password)
security.tokens.append(token)
clientService.set_options(wsse=security)

def get_admin(iccid):
    print("***** compose the SOAP body")
    #define iccid as a complext type
    getTerminalsDetailsRequest = dict(messageId="1001", version="1.0", licenseKey=license_key, iccid=iccid)

    print("***** SOAP request is:")
    #print getTerminalsDetailsRequest

    getTerminalsDetailsResponse = clientService.service.GetTerminalDetails(**getTerminalsDetailsRequest)

    print("***** SOAP response is:")
    print(getTerminalsByImsiResponse)
    #SACAR ADMIN Y NOMBRE SI SE PUEDE Y DEVOLVER COMO ARRAY
    admin = (getTerminalsDetailsResponse.terminals.terminal[0].accountId)
    return admin
    
def get_email (accountid)
    print("***** compose the SOAP body")
    #define imsi as a complext type
    getAccountDetailsRequest = dict(messageId="1001", version="1.0", licenseKey=license_key, accountids=long(accountid))

    print("***** SOAP request is:")
    #print getTerminalsDetailsRequest

    getAccountDetailsResponse = clientService.service.GetAccountDetails(**getAccountDetailsRequest)

    print("***** SOAP response is:")
    print(getTerminalsByImsiResponse)
    email = (getTerminalsDetailsResponse.terminals.terminal[0].accountId)
    return email
    
def deactivate_SIM(iccid, cust, date):
    print("***** compose the SOAP body")
    
    deactivateSIMRequest = dict(messageId="1001", version="1.0", licenseKey=license_key, strSIM=iccid, strCustPrefix=cust,  strDeactivationDate=date)

    print("***** SOAP request is:")
    #print getTerminalsDetailsRequest

     deactivateSIMResponse = clientService.service.GetTerminalDetails(**getTerminalsDetailsRequest)

    print("***** SOAP response is:")
    print(getTerminalsByImsiResponse)
    iccid = (getTerminalsDetailsResponse.terminals.terminal[0].accountId)
    return None
    
def get_location(iccid):
    print("***** compose the SOAP body")
    #define imsi as a complext type
    getLocationRequest = dict(messageId="1001", version="1.0", licenseKey=license_key, iccid=iccid)

    print("***** SOAP request is:")
    #print getTerminalsDetailsRequest

    getLocationResponse = clientService.service.GetLocation(**getLocationRequest)

    print("***** SOAP response is:")
    print(getTerminalsByImsiResponse)
    location = [(getLocationResponse.terminals.location.longitude),(getLocationResponse.terminals.location.latitude)
    return location

