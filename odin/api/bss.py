from odin.wrapper.proxy import BssCaller
from datetime import datetime
import re
from odin.api.helper import datetime2timestamp, timestamp2datetime, datetime_month_fistday, datetime_month_lastday

class Bss():
    """
    API to access the Odin BSS
    """
    
    def __init__(self, caller : BssCaller):
        self.__caller = caller
        
    def __call(self, server : str, api_name : str, params : list):
        """
        Call the remote server and get a list with data from Odin BSS
        
        """

        result = self.__caller.execute(server, api_name, params)
        """
        Odin BSS always return the result in this way: array['Result'] 
        """
        xmlrpc_result = result['Result']
        
        return xmlrpc_result
    
    
    def get_subscription(self, subscription_id):
        """ SubscriptionDetailsGet_API
        :param subscription_id: Subscription ID
        :type subscription_id: int
        
        :return: Basic data about a subscription: SubscriptionID, SubscriptionName, AccountID
        PlanID, PlanName, Status, ServStatus
        :rtype: dict 
        """
        xmlrpc_result = self.__call('BM', 'SubscriptionDetailsGet_API', [subscription_id])
        
        #The API always return the data in list format inside of another list: list[[data]] 
        data = xmlrpc_result[0]
        result = { 
            'SubscriptionID': data[0],
            'SubscriptionName': data[1],
            'AccountID': data[2],
            'PlanID': data[3],
            'PlanName': data[4],
            'Status': data[5],
            'ServStatus': data[6]
            }
        return result
    
    def get_subscription_extended(self, subscription_id):
        """ SubscriptionDetailsGetEx_API
        :param subscription_id: Subscription ID
        :type subscription_id: int

        :return: Datailed data about a subscription: SubscriptionID, SubscriptionName, AccountID
        PlanID, PlanName, Status, ServStatus, StartDate, ExpirationDate, LastBillDate,
        NextBillDate, BillingPeriodType, BillingPeriod, Trial, ShutdownDate, TerminateDate,
        Period, PeriodType, FreezePrices, PromoCode
        :rtype: dict
        """
        xmlrpc_result = self.__call('BM', 'SubscriptionDetailsGetEx_API', [subscription_id])
        
        #The API always return the data in list format inside of another list: list[[data]] 
        data = xmlrpc_result[0]
        result = { 
            'SubscriptionID': data[0],
            'SubscriptionName': data[1],
            'AccountID': data[2],
            'PlanID': data[3],
            'PlanName': data[4],
            'Status': data[5],
            'ServStatus': data[6],
            'StartDate': timestamp2datetime( data[7]),
            'ExpirationDate': timestamp2datetime( data[8]),
            'LastBillDate': timestamp2datetime( data[9]),
            'NextBillDate': timestamp2datetime( data[10]),
            'BillingPeriodType': data[11],
            'BillingPeriod': data[12],
            'Trial': data[13],
            'ShutdownDate': timestamp2datetime( data[14]),
            'TerminateDate': timestamp2datetime( data[15]),
            'Period': data[16],
            'PeriodType': data[17],
            'FreezePrices': data[18],
            'PromoCode': data[19]
            }
        return result

    def get_subscription_private(self, subscription_id):
        """ SubscriptionGet
        :param subscription_id: Subscription ID
        :type subscription_id: int

        :return: Detailed data about a subscription, the same information showd in the BA subscription
         general screen: SubscriptionID, SubscriptionName, AccountID, PlanID, NON1, Status, ServStatus,
         SubscriptionPeriod, startDate, ExpirationDate, ParentSubscriptionID, SetupFee, RecurringFee,
         RenewalFee, NonRefundableAmount, FullRefundPeriod, LastSyncDate, FreezePrices, TransferFee,
         NON3, BillingPeriodType, NON4, NON5, NON6, BillingPeriod, NON1, LastBillingDate,
         NextBillingDate, AutoRenewal, BillingModel, RenewOrderInterval, RecurringType, NON11.
         NON fields are not known
        :rtype: dict
        """
        xmlrpc_result = self.__call('BM', 'SubscriptionGet', [subscription_id])
        
        #The API always return the data in list format inside of another list: list[[data]] 
        data = xmlrpc_result[0]
        regex_search = '[^0-9.,]'
        regex_replace = ''
        result = { 
            'SubscriptionID': data[0],
            'SubscriptionName': data[1],
            'AccountID': data[2],
            'PlanID': data[3],
            'NON1': data[4],
            'Status': data[5],
            'ServStatus': data[6],
            'SubscriptionPeriod': data[7],
            'startDate': timestamp2datetime( data[8] ),
            'ExpirationDate': timestamp2datetime( data[9] ),
            'ParentSubscriptionID': data[10],
            'SetupFee': re.sub(regex_search, regex_replace, data[11]),
            'RecurringFee': re.sub(regex_search, regex_replace, data[12]),
            'RenewalFee': re.sub(regex_search, regex_replace, data[13]),
            'NonRefundableAmount': re.sub(regex_search, regex_replace, data[14]),
            'FullRefundPeriod': data[15],
            'LastSyncDate': timestamp2datetime( data[16] ),
            'FreezePrices': data[17],
            'TransferFee': re.sub(regex_search, regex_replace, data[18]),
            'NON2': data[19],
            'BillingPeriodType': data[20],
            'NON3': data[21],
            'NON4': data[22],
            'NON5': data[23],
            'BillingPeriod': data[24],
            'NON6': data[25],
            'LastBillingDate': timestamp2datetime( data[26] ),
            'NextBillingDate': timestamp2datetime( data[27] ),
            'AutoRenewal': data[28],
            'BillingModel': data[29],
            'RenewOrderInterval': data[30],
            'RecurringType': data[31],
            'NON7': data[32]
            }
        return result

    def get_last_to_serv_status_transition_date(self, subscription_id, serv_status):
        """ GetLastToServStatusTransitionDate_API
        :param subscription_id: Subscription ID
        :type subscription_id: int

        :param serv_status: Status of the service
        :type serv_status: int

        :return: Last transaction date from a service status: ServiceStatusLastDate
        :rtype: dict
        """
        xmlrpc_result = self.__call('BM', 'GetLastToServStatusTransitionDate_API', [subscription_id, serv_status])
        
        #The API always return the data in list format inside of another list: list[[data]] 
        data = xmlrpc_result[0]
        result = { 
            'ServiceStatusLastDate': timestamp2datetime( data[0])
            }
        return result

    def get_subscription_param_value(self, subscription_id, param_id):
        """ SubscrParamValueGet_API
        :param subscription_id: Subscription ID
        :type subscription_id: int

        :param param_id: Status of the service
        :type param_id: int

        :return: Value of specific parameter
        :rtype: dict
        """
        xmlrpc_result = self.__call('BM', 'SubscrParamValueGet_API', [subscription_id, param_id])
        
        #The API always return the data in list format inside of another list: list[[data]] 
        data = xmlrpc_result[0]
        result = { 
            'ParameterValue': data[0],
            }
        return result
    
    def get_domain(self, full_domain_name):
        """ DomainInfoGet_API
        :param full_domain_name: Full Domain Name (domain.com.br)
        :type full_domain_name: str

        :return: Data about the account owner of the domain: AccountID, VendorID, DomainID, FullDomainName, DomainZoneID, 
        Status, External DNS, RegistrationPeriod, startDate, ExpirationDate, 
        PrimaryNameServer, SecondaryNameServer, ThirdNameServer, FourthNameSever, 
        CompanyName, FName, MName, LName, Email, getPhone, getFax, FName, MName, LName, 
        Email, getPhone, getFax, FName, MName, LName, Email, getPhone, getFax, FName, 
        MName, LName, Email, getPhone, getFax
        :rtype: dict
        """
        xmlrpc_result = self.__call('DOMAINGATE', 'DomainInfoGet_API', [full_domain_name])
        
        #The API always return the data in list format inside of another list: list[[data]] 
        data = xmlrpc_result[0]
        result = { 
            'AccountID': data[0],
            'VendorID': data[1],
            'DomainID': data[2],
            'FullDomainName': data[3],
            'DomainZoneID': data[4],
            'Status': data[5],
            'External DNS': data[6],
            'RegistrationPeriod': data[7],
            'startDate': timestamp2datetime(data[8]),
            'ExpirationDate': timestamp2datetime(data[9]),
            'PrimaryNameServer': data[10],
            'SecondaryNameServer': data[11],
            'ThirdNameServer': data[12],
            'FourthNameSever': data[13],
            'CompanyName': data[14],
            'PersonalContactFName': data[15],
            'PersonalContactMName': data[16],
            'PersonalContactLName': data[17],
            'PersonalContactEmail': data[18],
            'PersonalContactgetPhone': data[19],
            'PersonalContactgetFax': data[20],
            'AdminContactFName': data[21],
            'AdminContactMName': data[22],
            'AdminContactLName': data[23],
            'AdminContactEmail': data[24],
            'AdminContactgetPhone': data[25],
            'AdminContactgetFax': data[26],
            'BillingContactFName': data[27],
            'BillingContactMName': data[28],
            'BillingContactLName': data[29],
            'BillingContactEmail': data[30],
            'BillingContactgetPhone': data[31],
            'BillingContactgetFax': data[32],
            'TechContactFName': data[33],
            'TechContactMName': data[34],
            'TechContactLName': data[35],
            'TechContactEmail': data[36],
            'TechContactgetPhone': data[37],
            'TechContactgetFax': data[38]
            }
        return result
    
    def get_plan_details(self, plan_id):
        """ PlanDetailsGet_API
        :param plan_id: Plan ID
        :type plan_id: int
        :return: Data about the plan: PlanID, Name, CategoryID, ResourceCurrencyID, ShortDescription, 
        LongDescription, GateName, GroupID, IsParentReq, RecurringType, BillingPeriodType, 
        BillingPeriod, ShowPriority, Default_PlanPeriodID, IsOTFI, DocID, VendorAccountID, 
        ServiceTemplateID, PricePeriodType, Published
        :rtype: dict
        """
        xmlrpc_result = self.__call('BM', 'PlanDetailsGet_API', [plan_id])
        
        #The API always return the data in list format inside of another list: list[[data]] 
        data = xmlrpc_result[0]
        result = { 
            'PlanID': data[0],
            'Name': data[1],
            'CategoryID': data[2],
            'ResourceCurrencyID': data[3],
            'ShortDescription': data[4],
            'LongDescription': data[5],
            'GateName': data[6],
            'GroupID': data[7],
            'IsParentReq': data[8],
            'RecurringType': data[9],
            'BillingPeriodType': data[10],
            'BillingPeriod': data[11],
            'ShowPriority': data[12],
            'Default_PlanPeriodID': data[13],
            'IsOTFI': data[14],
            'DocID': data[15],
            'VendorAccountID': data[16],
            'ServiceTemplateID': data[17],
            'PricePeriodType': data[18],
            'Published': data[19],
            }
        return result
    
    def get_plan_category_list(self, vendor_id, sort_number=-1):
        """ PlanCategoryListGet_API
        :param vendor_id: Vendor ID
        :type vendor_id: int

        :param sort_number: defines how output data is sorted. 1 for the first filed, 2 for the second, etc. Positive number
        order the sort is ascending and negative is descending
        :type sort_number: int
        :return: Data about plan category: PlanCategoryID, Name, Description
        :rtype: list of dict
        """
        xmlrpc_result = self.__call('BM', 'PlanCategoryListGet_API', [vendor_id, sort_number])
        
        #The API always return the data in list format inside of another list: list[[data]] 
        data = xmlrpc_result[0]
        result = []
        for line in data:
            result.append( { 
                'PlanCategoryID': line[0],
                'Name': line[1],
                'Description': line[2]
                }
            )
        return result
    
    def get_rate_full_list(self, plan_id, sort_number=-1):
        """ PlanRateListFullGet_API
        :param plan_id: Plan ID
        :type plan_id: int

        :param sort_number: defines how output data is sorted. 1 for the first filed, 2 for the second, etc. Positive number
        order the sort is ascending and negative is descending
        :type sort_number: int

        :return: All rates from a plan: ResourceRateID, ResourceRateName, Description, Included_Value, Upper_Limit, 
        Lower_Limit, Unit_of_Measure, Setup_Fee, Recurring_Fee, Measurable, ResourceID, 
        SetupFeeDescr, RecurrFeeDescr, IsVisible, IsMain, StoreText, IsSFperUnit, IsRFperUnit, 
        IsSFforUpgrade, StorePriceText, ResourceCategoryID, SortOrder, IsOveruseFeeTiered,
         IsRecurringFeeTiered, IsSetupFeeTiered
         :rtype: list of dict
        """
        xmlrpc_result = self.__call('BM', 'PlanRateListFullGet_API', [plan_id, sort_number])
        
        #The API always return the data in list format inside of another list: list[[data]] 
        data = xmlrpc_result[0]
        result = []
        for line in data:
            result.append( { 
                'ResourceRateID': line[0],
                'ResourceRateName': line[1],
                'Description': line[2],
                'Included_Value': line[3],
                'Upper_Limit': line[4],
                'Lower_Limit': line[5],
                'Unit_of_Measure': line[6],
                'Setup_Fee': line[7],
                'Recurring_Fee': line[8],
                'Measurable': line[9],
                'ResourceID': line[10],
                'SetupFeeDescr': line[11],
                'RecurrFeeDescr': line[12],
                'IsVisible': line[13],
                'IsMain': line[14],
                'StoreText': line[15],
                'IsSFperUnit': line[16],
                'IsRFperUnit': line[17],
                'IsSFforUpgrade': line[18],
                'StorePriceText': line[19],
                'ResourceCategoryID': line[20],
                'SortOrder': line[21],
                'IsOveruseFeeTiered': line[22],
                'IsRecurringFeeTiered': line[23],
                'IsSetupFeeTiered': line[24],
                }
            )
        return result
    
    def get_plan_period_list(self, plan_id, sort_number=2):
        """ PlanPeriodListGet_API
        :param plan_id: Plan ID
        :type plan_id: int

        :param sort_number: defines how output data is sorted. 1 for the first filed, 2 for the second, etc. Positive number
        order the sort is ascending and negative is descending
        :type sort_number: int

        :return: All periods of a plan: PlanPeriodID, Period, PeriodType, Trial, SetupFee, SubscriptionFee,
        RenewalFee, TransferFee, NonRefundableAmount, RefundPeriod, Enabled, NumberOfPeriods,
        FeeText, SortNumber, IsOTFI, DepositFee, DepositDescr
        :rtype: list of dict
        """
        xmlrpc_result = self.__call('BM', 'PlanPeriodListGet_API', [plan_id, sort_number])
        
        #The API always return the data in list format inside of another list: list[[data]] 
        data = xmlrpc_result[0]
        result = []
        for line in data:
            result.append( { 
                'PlanPeriodID': line[0],
                'Period': line[1],
                'PeriodType': line[2],
                'Trial': line[3],
                'SetupFee': line[4],
                'SubscriptionFee': line[5],
                'RenewalFee': line[6],
                'TransferFee': line[7],
                'NonRefundableAmount': line[8],
                'RefundPeriod': line[9],
                'Enabled': line[10],
                'NumberOfPeriods': line[11],
                'FeeText': line[12],
                'SortNumber': line[13],
                'IsOTFI': line[14],
                'DepositFee': line[15],
                'DepositDescr': line[16]
                }
            )
        return result

    def get_plan_category_details(self, plan_category_id):
        """ PlanCategoryDetailsGet_API
        :param plan_category_id: Plan Category ID
        :type plan_category_id: int

        :return: Detail about a plan category: planCategoryID, name, description, AccountID
        :rtype: dict
        """
        xmlrpc_result = self.__call('BM', 'PlanCategoryDetailsGet_API', [plan_category_id])
        
        #The API always return the data in list format inside of another list: list[[data]] 
        data = xmlrpc_result[0]
        result = { 
            'planCategoryID': data[0],
            'name': data[1],
            'description': data[2],
            'AccountID': data[3]
            }
        return result

    def get_customer_subscription_list(self, account_id, sort_number=-1):
        """ GetCustomerSubscriptionList_API
        :param account_id: Account (customer) ID
        :type account_id: int

        :param sort_number: defines how output data is sorted. 1 for the first filed, 2 for the second, etc. Positive number
        order the sort is ascending and negative is descending
        :type sort_number: int

        :return: All subscription from a account: SubscriptionID, SubscriptionName, PlanID, PlanName, 
        PlanPeriodID, Period, PeriodType, StartDate, ExpirationDate, Status, ServStatus, ContainerName
        :rtype: list of dict
        """
        xmlrpc_result = self.__call('BM', 'GetCustomerSubscriptionList_API', [account_id, sort_number])
        
        #The API always return the data in list format inside of another list: list[[data]] 
        data = xmlrpc_result[0]
        result = []
        for line in data:
            result.append( { 
                'SubscriptionID': line[0],
                'SubscriptionName': line[1],
                'PlanID': line[2],
                'PlanName': line[3],
                'PlanPeriodID': line[4],
                'Period': line[5],
                'PeriodType': line[6],
                'StartDate': timestamp2datetime(line[7]),
                'ExpirationDate': timestamp2datetime(line[8]),
                'Status': line[9],
                'ServStatus': line[10],
                'ContainerName': line[11]
                }
            )
        return result

    def get_subsctiption_by_resource_list(self, resource_rate_id, sort_number=-1):
        """ SubscriptionListByResourceRateGet_API
        :param resource_rate_id: Resource Rate ID
        :type resource_rate_id: int

        :param sort_number: defines how output data is sorted. 1 for the first filed, 2 for the second, etc. Positive number
        order the sort is ascending and negative is descending
        :type sort_number: int

        :return: All subscriptions that have the resource rate: SubscriptionID, SubscriptionName, PlanID, PlanName,
        PlanPeriodID, Status, ServStatus
        :rtype: list of dict
        """
        xmlrpc_result = self.__call('BM', 'SubscriptionListByResourceRateGet_API', [resource_rate_id, sort_number])
        
        #The API always return the data in list format inside of another list: list[[data]] 
        data = xmlrpc_result[0]
        result = []
        for line in data:
            result.append( { 
                'SubscriptionID': line[0],
                'SubscriptionName': line[1],
                'PlanID': line[2],
                'PlanName': line[3],
                'PlanPeriodID': line[4],
                'Status': line[5],
                'ServStatus': line[6]
                }
            )
        return result

    def get_subsctiption_resources_list(self, subscription_id, sort_number=1):
        """ SubscriptionResourcesListGet_API
        :param subscription_id: Subscription ID
        :type subscription_id: int

        :param sort_number: defines how output data is sorted. 1 for the first filed, 2 for the second, etc. Positive number
        order the sort is ascending and negative is descending
        :type sort_number: int

        :return: All resources and resources rate from a subscription: ResourceID, ResourceRateID, ResourceName, StoreDescription, 
        StorePriceText, StoreSortOrder, Status, Resource Category, IncludedAmount, AdditionalAmount, UsedAmount, 
        OrderedAmount, Unit, MinUnits, MaxUnits, Measurable, RelativeStatus, OrderNumber, SetupFee, 
        RecurringFee, OveruseFee, Location, IsOveruseFeeTiered, IsRecurringFeeTiered, IsSetupFeeTiered
        :rtype: list of dict
        """
        xmlrpc_result = self.__call('BM', 'SubscriptionResourcesListGet_API', [subscription_id, sort_number])
        
        #The API always return the data in list format inside of another list: list[[data]] 
        data = xmlrpc_result[0]
        result = []
        for line in data:
            result.append( { 
                'ResourceID': line[0],
                'ResourceRateID': line[1],
                'ResourceName': line[2],
                'StoreDescription': line[3],
                'StorePriceText': line[4],
                'StoreSortOrder': line[5],
                'Status': line[6],
                'Resource Category': line[7],
                'IncludedAmount': line[8],
                'AdditionalAmount': line[9],
                'UsedAmount': line[10],
                'OrderedAmount': line[11],
                'Unit': line[12],
                'MinUnits': line[13],
                'MaxUnits': line[14],
                'Measurable': line[15],
                'RelativeStatus': line[16],
                'OrderNumber': line[17],
                'SetupFee': line[18],
                'RecurringFee': line[19],
                'OveruseFee': line[20],
                'Location': line[21],
                'IsOveruseFeeTiered': line[22],
                'IsRecurringFeeTiered': line[23],
                'IsSetupFeeTiered': line[24]
                }
            )
        return result
    
    def get_order_by_status(self, order_type_id='', order_status_id='', order_start_time=None, order_end_time=None, vendor_id=1, sort_number=1):
        """ OrderByStatusListGet_API
        :param order_type_id: Order Type ID ('SO', 'CH', etc)
        :type order_type_id: str

        :param order_status_id: Order Status ID ('C1', 'NW', etc)
        :type order_status_id: str

        :param order_start_time: Start date
        :type order_start_time: datetime

        :param order_end_time: End date
        :type order_end_time: datetime

        :param vendor_id: Vendor ID
        :type vendor_id: int

        :param sort_number: defines how output data is sorted. 1 for the first filed, 2 for the second, etc. Positive number
        order the sort is ascending and negative is descending
        :type sort_number: int

        :return: List of orders: OrderID, OrderNumber, CustomerID, CustomerName, OrderStatus, 
        OrderType, CreationTime, OrderDate, Total, TaxTotal, DiscountTotal, MerchTotal, ExpirationDate, 
        PromoCode, SalesBranchID, SalesBranchName, SalesPersonID, SalesPersonName, Comments
        :rtype: list of dict
        """
        
        if not vendor_id:
            raise Exception("'vendor_id cannot be null")
        
        if not order_start_time:
            order_start_time = datetime_month_fistday( datetime.now() )
        
        if not order_end_time:
            order_end_time = datetime_month_lastday( datetime.now() )
        
        xmlrpc_result = self.__call('BM', 'OrderByStatusListGet_API', [vendor_id, order_type_id, order_status_id, datetime2timestamp(order_start_time), datetime2timestamp(order_end_time), sort_number])
        
        #The API always return the data in list format inside of another list: list[[data]] 
        data = xmlrpc_result[0]
        result = []
        for line in data:
            result.append( { 
                'OrderID': line[0],
                'OrderNumber': line[1],
                'CustomerID': line[2],
                'CustomerName': line[3],
                'OrderStatus': line[4],
                'OrderType': line[5],
                'CreationTime': timestamp2datetime( line[6] ),
                'OrderDate': timestamp2datetime( line[7] ),
                'Total': line[8],
                'TaxTotal': line[9],
                'DiscountTotal': line[10],
                'MerchTotal': line[11],
                'ExpirationDate': timestamp2datetime( line[12] ),
                'PromoCode': line[13],
                'SalesBranchID': line[14],
                'SalesBranchName': line[15],
                'SalesPersonID': line[16],
                'SalesPersonName': line[17],
                'Comments': line[18]
                }
            )
        return result
        
    def get_sales_order_by_subsctiption(self, subscription_id, sort_number=1):
        """ SalesOrderGetSalesOrderBySubscList (method not included in the public API and shouldn't be used)
        :param subscription_id: Subscription ID
        :type subscription_id: int

        :param sort_number: defines how output data is sorted. 1 for the first filed, 2 for the second, etc. Positive number
        order the sort is ascending and negative is descending
        :type sort_number: int

        :return: List of orders for a subscription: OrderID, OrderNumber, OrderType, OrderDate, StatusIcon, Status
        OrderValue, TimeWait, User
        :rtype: list of dict
        """
        
        xmlrpc_result = self.__call('BM', 'SalesOrderGetSalesOrderBySubscList', [subscription_id, sort_number])
        
        #The API always return the data in list format inside of another list: list[[data]] 
        data = xmlrpc_result[0]
        result = []
        for line in data:
            result.append( { 
                'OrderID': line[0],
                'OrderNumber': line[1],
                'OrderType': line[2],
                'OrderDate': timestamp2datetime( line[3] ),
                'StatusIcon': line[4],
                'Status': line[5],
                'OrderValue': line[6],
                'TimeWait': line[7],
                'User': line[8]
                }
            )
        return result
        
    def get_order(self, order_id):
        """ GetOrder_API
        :param order_id: Order ID
        :type order_id: int

        :return: Details of an order: OrderID, OrderNumber, VendorAccountID, CustomerID, OrderStatusID, OrderTypeID, 
        CreationTime, OrderDate, Total, TaxTotal, DiscountTotal, MerchTotal, Comments, ExpirationDate,
        PromoCode, SalesBranchID, SalesPersonID, CurrencyID, CompletedDate
        :rtype: dict
        """
        xmlrpc_result = self.__call('BM', 'GetOrder_API', [order_id])
        
        #The API always return the data in list format inside of another list: list[[data]] 
        data = xmlrpc_result[0]
        result = { 
            'OrderID': data[0],
            'OrderNumber': data[1],
            'VendorAccountID': data[2],
            'CustomerID': data[3],
            'OrderStatusID': data[4],
            'OrderTypeID': data[5],
            'CreationTime': timestamp2datetime( data[6] ),
            'OrderDate': timestamp2datetime( data[7] ),
            'Total': data[8],
            'TaxTotal': data[9],
            'DiscountTotal': data[10],
            'MerchTotal': data[11],
            'Comments': data[12],
            'ExpirationDate': timestamp2datetime( data[13] ),
            'PromoCode': data[14],
            'SalesBranchID': data[15],
            'SalesPersonID': data[16],
            'CurrencyID': data[17],
            'CompletedDate': timestamp2datetime( data[18] )
            }
        return result
    
    def get_subscription_list_by_order(self, order_id, sort_number=1):
        """ GetSubscriptionsListByOrder_API
        :param order_id: Order ID
        :type order_id: int

        :param sort_number: defines how output data is sorted. 1 for the first filed, 2 for the second, etc. Positive number
        order the sort is ascending and negative is descending
        :type sort_number: int

        :return: Get all subscription generated by one order: SubscriptionID
        :rtype: list of dict
        """
        xmlrpc_result = self.__call('BM', 'GetSubscriptionsListByOrder_API', [order_id, sort_number])
        
        #The API always return the data in list format inside of another list: list[[data]] 
        data = xmlrpc_result[0]
        result = []
        for line in data:
            result.append( { 
                'SubscriptionID': line[0]
                }
            )
        return result
        
    def get_order_fin_details_list(self, order_id, sort_number=1):
        """ OrderFinDetailsListGetExt_API
        :param order_id: Order ID
        :type order_id: int

        :param sort_number: defines how output data is sorted. 1 for the first filed, 2 for the second, etc. Positive number
        order the sort is ascending and negative is descending
        :type sort_number: int

        :return: Details with SKU from an order: DetailID, SKU, Description, Quantity, UOM, Duration, Period,
        UnitPrice, TaxCategory, DiscountAmount, ExtendedPrice, StartDate, EndDate, Subscription, DetailType,
        ResourceDescription
        :rtype: list of dict
        """
        xmlrpc_result = self.__call('BM', 'OrderFinDetailsListGetExt_API', [order_id, sort_number])
        
        #The API always return the data in list format inside of another list: list[[data]] 
        data = xmlrpc_result[0]
        result = []
        for line in data:
            result.append( { 
                'DetailID': line[0],
                'SKU': line[1],
                'Description': line[2].replace('&#32;', ''),
                'Quantity': line[3],
                'UOM': line[4],
                'Duration': line[5],
                'Period': line[6],
                'UnitPrice': float(line[7].replace('BRL ', '')),
                'TaxCategory': line[8],
                'DiscountAmount': float(line[9].replace('BRL ', '')),
                'ExtendedPrice': float(line[10].replace('BRL ', '')),
                'StartDate': timestamp2datetime( line[11] ),
                'EndDate': timestamp2datetime( line[12] ),
                'Subscription': line[13],
                'DetailType': line[14],
                'ResourceDescription': line[15]
                }
            )
        return result

    def send_notification(self, template_name, subscription_id, user_id, place_holders={}):
        """ SendSubscriptionNotificationForUser_API
        :param templace_name: Email template. It is the name of the notification template
        :type templace_name: string

        :param subscription_id: Subscription ID
        :type subscription_id: int

        :param user_id: User from the subscription
        :type user_id: int

        :param user_id: List with key values with parameters to be send to the email template
        :type user_id: dict

        :return: {'Status': 'Operation done. '} if success
        :rtype: list of dict
        """
        
        params = [template_name, subscription_id, user_id]
        for key, value in place_holders.items():
            params.append(key)
            params.append(value)
        
        xmlrpc_result = self.__call('MESSAGE', 'SendSubscriptionNotificationForUser_API', params)
        
        #The API always return the data in list format inside of another list: list[[data]] 
        result = xmlrpc_result[0]
        return result