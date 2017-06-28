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
    #We compose the SOAP body for the GetLocationRequest with the accountid we get from the previous function
    getLocationRequest = dict(messageId="1001", version="1.0", licenseKey=license_key, iccid=iccid)

    #We send to Jasper our SOAP request with the function in the WSDL file GetTerminalDetails and get the response in a variable
    getLocationResponse = clientService.service.GetLocation(**getLocationRequest)

    longitude = getLocationResponse.terminals.location.longitude
    latitude = getLocationResponse.terminals.location.latitude
    #This function has been implemented by a 3rd party company and it is only for its use. For continue the developing of the project
    #we will simulate the coordinates of the SIM card.
    return longitude, latitude

iccid = "89302720396916796910"
t=0
if t== 0:
  get_email(iccid)
  t = t+1
