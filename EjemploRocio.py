# -*- coding: utf-8 -*-
class GetTerminalsByImsi:

    def __init__(self,imsi):
        import logging
        import ssl
        from time import sleep
        from suds.client import Client
        from suds.wsse import Security,UsernameToken
        #from common.soap import ReadSecurityFile

        print("***** read api_security.ini to get the username, password, etc")
        service='terminal'
        wsdlurl='https://api.jasper.com/ws/schema/Terminal.wsdl'
        username='username'
        password='password'
        license_key='licenseKey'

        #wsdlurl= ReadSecurityFile(service).wsdlurl
        #username= ReadSecurityFile(service).username
        #password= ReadSecurityFile(service).password
        #license_key= ReadSecurityFile(service).license_key

        # disable certificate verification
        ssl._create_default_https_context = ssl._create_unverified_context

        logging.basicConfig(level=logging.INFO)
        #logging.getLogger('suds.client').setLevel(logging.DEBUG)
        #logging.getLogger('suds.transport').setLevel(logging.DEBUG)
        #logging.getLogger('suds.suds.xsd.schema').setLevel(logging.DEBUG)
        #logging.getLogger('suds.wsdl').setLevel(logging.DEBUG)


        print("***** create the SOAP client")
        clientService = Client(wsdlurl)
        print (clientService)

        print("***** compose the SOAP security header")
        # add WSSE
        security = Security()
        token = UsernameToken(username, password)
        security.tokens.append(token)
        clientService.set_options(wsse=security)

        print("***** compose the SOAP body")
        #define imsi as a complext type
        imsi = dict(imsi=imsi)
        getTerminalsByImsiRequest = dict(messageId="1001", version="1.0", licenseKey=license_key, imsi=imsi)

        print("***** SOAP request is:")
        print (getTerminalsByImsiRequest)

        getTerminalsByImsiResponse = clientService.service.GetTerminalsByImsi(**getTerminalsByImsiRequest)

        print("***** SOAP response is:")
        print(getTerminalsByImsiResponse)
        iccid = (getTerminalsByImsiResponse.terminals.terminal[0].iccid)
        print(iccid)


miClase = GetTerminalsByImsi('incluirICCID')
