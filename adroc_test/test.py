from config.test_config import *
from odin.wrapper.proxy import BssCaller
from odin.wrapper.proxy import OssCaller
from odin.api.bss import Bss 
from odin.api.oss import Oss 

def getMethods(class_object):
    all_methods = {}
    counter = 0
    class_list = dir(class_object)
    for method_name in class_list:
        if not method_name.startswith('_'):
            counter += 1
            all_methods[counter] = method_name
    return all_methods

def menu():
    bss_caller = BssCaller(bss_server_url)
    bss = Bss(bss_caller)
    
    oss_caller = OssCaller(oss_server_url)
    oss = Oss(oss_caller)

    while(True):
        system_option = input( "Choose 0=Exit 1-BA, 2-OSA: ")
        print(system_option)
        if(system_option == '1'):
            method_list = getMethods(Bss)
        elif(system_option == '2'):
            method_list = getMethods(Oss)
        elif(system_option == '0'):
            break
        else:
            continue
    
        print("List of function: ")
        for key, value in method_list.items():
            print(key, value)
    
        function_option = int(input( "Choose one function: "))
    
        try:
        ####################  
        ### OSA
        ####################  
            if(method_list[function_option] == 'get_subscription_token'): 
                  
                result = oss.get_subscription_token(account_id, subscription_id)
                print(result)
                  
            elif(method_list[function_option] == 'get_services_instances'): 
                  
                result = oss.get_services_instances(application_instance_id)
                print(result)
        
            elif(method_list[function_option] == 'get_application_instances'): 
                  
                result = oss.get_application_instances(app_id)
                print(result)
        
        ####################  
        ### BA
        ####################  
            elif(method_list[function_option] == 'get_subscription'):
                result = bss.get_subscription(subscription_id)
                print(result)
                
            elif(method_list[function_option] == 'get_subscription_extended'): 
                
                result = bss.get_subscription_extended(subscription_id)
                print(result)
                
            elif(method_list[function_option] == 'get_last_to_serv_status_transition_date'): 
                
                result = bss.get_last_to_serv_status_transition_date(subscription_id, serv_status)
                print(result)
                
            elif(method_list[function_option] == 'get_subscription_param_value'): 
                
                result = bss.get_subscription_param_value(subscription_param_id, param_id)
                print(result)
                
            elif(method_list[function_option] == 'get_domain'): 
                
                result = bss.get_domain(full_domain_name)
                print(result)
                
            elif(method_list[function_option] == 'get_plan_details'): 
                
                result = bss.get_plan_details(plan_id)
                print(result)
                
            elif(method_list[function_option] == 'get_plan_category_list'): 
                
                result = bss.get_plan_category_list(vendor_id)
                print(result)
                
            elif(method_list[function_option] == 'get_rate_full_list'): 
                
                result = bss.get_rate_full_list(plan_id)
                print(result)
                
            elif(method_list[function_option] == 'get_plan_period_list'): 
                
                result = bss.get_plan_period_list(plan_id)
                print(result)
                
            elif(method_list[function_option] == 'get_plan_category_details'): 
                
                result = bss.get_plan_category_details(plan_category_id)
                print(result)
                
            elif(method_list[function_option] == 'get_customer_subscription_list'): 
                
                result = bss.get_customer_subscription_list(account_id)
                print(result)
                
            elif(method_list[function_option] == 'get_subsctiption_by_resource_list'): 
                result = bss.get_subsctiption_by_resource_list(resource_rate_id)
                print(result)
                
            elif(method_list[function_option] == 'get_subsctiption_resources_list'): 
                
                result = bss.get_subsctiption_resources_list(subscription_id)
                print(result)
                
            elif(method_list[function_option] == 'get_order_by_status'): 
                
                result = bss.get_order_by_status('SO', 'C2')
                print(result)
                
            elif(method_list[function_option] == 'get_sales_order_by_subsctiption'): 
                
                result = bss.get_sales_order_by_subsctiption(subscription_id)
                print(result)
                
            elif(method_list[function_option] == 'get_order'): 
                
                result = bss.get_order(order_id)
                print(result)
                
            elif(method_list[function_option] == 'get_subscription_list_by_order'): 
                
                result = bss.get_subscription_list_by_order(order_id)
                print(result)
                
            elif(method_list[function_option] == 'get_order_fin_details_list'): 
                
                result = bss.get_order_fin_details_list(order_id)
                print(result)
                
            elif(method_list[function_option] == 'send_notification'): 
                result = bss.send_notification(template_name, subscription_id, user_id, place_holders)
                print(result)
                
            elif(method_list[function_option] == 'get_subscription_private'): 
                
                result = bss.get_subscription_private(subscription_id)
                print(result)
            
            else:
                print("Wrong option: ", function_option)
    
        except Exception as ex:
            print("ERROR: ", ex)
        