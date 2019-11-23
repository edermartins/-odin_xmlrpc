from odin.wrapper.proxy import OssCaller

class Oss():
    """
    API to access the Odin OSS
    """
    
    def __init__(self, caller : OssCaller):
        self.__caller = caller
        
    def __call(self, api_name : str, params : list):
        """
        Call the remote server and get a list with data from Odin BSS
        
        """

        result = self.__caller.execute(api_name, params)
        if 'error_message' in result:
            raise Exception(result['error_message'])
        
        """
        Odin OSA always return the result in this way: dict{'result' : {data}} 
        """
        return result['result']
    
    def get_subscription_token(self, account_id, subscript_id):
        """ pem.APS.getSubscriptionToken
        :param account_id: Account ID
        :type account_id: int
        
        :param subscript_id: Subscription ID
        :type subscript_id: int
        
        :return: Token for an specific account: aps_token, controller_uri 
        :rtype: dict
        
        """
        parameters = {"account_id": account_id, "subscript_id" : subscript_id}
        xmlrpc_result = self.__call('pem.APS.getAccountToken', parameters)
        
        #The API always return an [{...data...}] 
        return xmlrpc_result
    
    def get_services_instances(self, application_instance_id, service_id=''):
        """ pem.APS.getServiceInstances
        :param application_instance_id: Application Instance ID
        :type application_instance_id: int
        
        :param service_id: Service ID
        :type service_id: str
         :return: Instances of a application: Depends of the APS instance
         :rtype: list of dict
        """
        parameters = {"application_instance_id": application_instance_id, "service_id" : service_id}
        xmlrpc_result = self.__call('pem.APS.getServiceInstances', parameters)
        
        #The API always return an [{...data...}]
        return xmlrpc_result
    
    def get_application_instances(self, app_id, subscription_id=''):
        """ pem.APS.getApplicationInstances
        :param app_id: Application ID
        :type app_id: int
        
        :param subscription_id: Subscription ID. This parameter is optional. If it is not provided, then all 
                             Application Instance IDs from all subscriptions are returned.
        :type subscription_id: int

         :return: Instances of a application: application_instance_id, application_resource_id
         :rtype: list of dict
        """
        parameters = {}
        parameters["app_id"] = app_id
        if(subscription_id != ''):
            parameters["subscription_id"] = subscription_id

        xmlrpc_result = self.__call('pem.APS.getApplicationInstances', parameters)
        
        #The API always return an [{...data...}]
        return xmlrpc_result