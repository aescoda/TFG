from suds.client import Client
from suds.wsse import Security,UsernameToken

def get_email(accountid):

    wsdlurl= "http://apitest.jasperwireless.com/ws/schema/Account.wsdl"
    username="aescodaAPI"
    password= "!1994Whor5qp"
    license_key= "7c41495d-5047-4d2c-b01c-e5cb91ce6756"
    
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
    accountid = dict(accountid = accountid)
    getAccountDetailsRequest = dict(messageId="1001", version="1.0", licenseKey=license_key, accountids=accountid)

    #We send to Jasper our SOAP request with the function in the WSDL file GetTerminalDetails and get the response in a variable
    getAccountDetailsResponse = clientService.service.GetAccountDetails(**getAccountDetailsRequest)
    print getAccountDetailsResponse
    #We parse the SOAP response to find the value we need of the SIM card and return it
    email = getAccountDetailsResponse.accounts.account.billing.contact.email
    name = getAccountDetailsResponse.accounts.account.billing.contact.name
    print email
    print name
    return None
accountid = 100000538
t=0
if t==0:
  get_email(accountid)
  t=t+1
