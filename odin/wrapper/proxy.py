from xmlrpc import client
import base64

class Caller(object):
    """
    This class wraps a xmlrpc call
    """    
    def __init__(self, server_url, transport=None, encoding=None, verbose=False,
                 allow_none=False, use_datetime=False, use_builtin_types=False,
                 context=None):
        if not server_url:
            raise Exception('The parameter server_url cannot be null')

        # Creates a proxy rpc
        self._proxy = client.ServerProxy(server_url, transport=None, encoding=None, verbose=False,
                 allow_none=False, use_datetime=False, use_builtin_types=False,
                 context=None)
        
class BssCaller(Caller):
        
    def execute(self, server='BM', api_name=None, params=None):
        """
        BSS Odin RPC Execute method
        :param server: Odin has few containers called servers: BM, DOMAINGATE, MESSAGE
        :type server: str
        
        :param api_name: Is the name of the Odin BSS API
        :type api_name: str
        
        :param params: list with the parameters values
        :type params: list
        
        :return: The RPC result from Odin BSS Server
        :rtype: mixed
        """
        
        if not server or not isinstance(server, str):
            raise Exception('server is empty, null or is not a string') 
        
        if not api_name or not isinstance(api_name, str):
            raise Exception('api_name is empty, null or is not a string') 
        
        if not params or not isinstance(params, list):
            raise Exception('method is empty, null or is not a list') 
        
        parameters = {"Server":server, "Method": api_name, "Params" : params}
        
        try:
            result = self._proxy.Execute(parameters)
        
        except client.Fault as error:
            raise Exception(format(base64.b64decode(error.faultString)))
        
        except client.ProtocolError as error:
            raise Exception("""A protocol error occurred
        URL: {}
        HTTP/HTTPS headers: {}
        Error code: {}
        Error message: {}""".format(
                error.url, error.headers, error.errcode, error.errmsg))
        
        except ConnectionError as error:
            raise Exception("Connection error. Is the server running? {}".format(error))
        
        return result

class OssCaller(Caller):
    
    def execute(self, api_name=None, params=None):
        """
        OSS Odin RPC Execute method
        :param api_name: Is the name of the Odin BSS API
        :type api_name: str

        :param params: list with the parameters values
        :type params: list
        
        :return: The RPC result from Odin BSS Server
        :rtype: mixed
        """
        
        if not api_name or not isinstance(api_name, str):
            raise Exception('api_name is empty, null or is not a string') 
        
        if not params or not isinstance(params, dict):
            raise Exception('method is empty, null or is not a dict') 

        try:
            # get the proxy function dynacally
            func = getattr(self._proxy, api_name)
            # calls the RPC remote function
            result = func(params)
        
        except client.Fault as error:
            raise Exception(format(base64.b64decode(error.faultString)))
        
        except client.ProtocolError as error:
            raise Exception("""A protocol error occurred
        URL: {}
        HTTP/HTTPS headers: {}
        Error code: {}
        Error message: {}""".format(
                error.url, error.headers, error.errcode, error.errmsg))
        
        except ConnectionError as error:
            raise Exception("Connection error. Is the server running? {}".format(error))
        
        return result
