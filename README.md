# Python Port of Odin API RPC

Both BA (BSS) and OSA (OSS) was ported to Python 3 and are part of [Premium Odin Service Automation](https://be.ingrammicro.eu/en/impartner/cloud/odin-service-platform-automation "Premium Odin Service Automation").

I based all the services in the Premium Odin Service Automation [7.4](https://docs.cloudblue.com/oa/7.4/premium/content/home.htm "7.4") and [8.2](https://docs.cloudblue.com/oa/8.2/premium/content/home.htm "8.2") versions.

### How to import it using PIP

`pip install git+https://github.com/edermartins/odin_xmlrpc#egg=odin`

Or you also can just copy it into you project.

### How to test
There are two ways do do it. A very simple interactive test (addroc can test one function at time) and unittest (call all methods).


#### 1.Addroc

This test is like a little interactive system. You can choose what you want to test.

Copy the template file `adroc_test/test_config.py.template` to `adroc_test/test_config.py` and fill it with your Odin data.

At project root type `python` and call the tester:

```python
>>> import adroc_test.test as test
>>> test.menu()
Choose 0=Exit 1-BA, 2-OSA:
```
Type 1 for BA implemented API and 2 for OSA and the tester will shows a list of API.
Just type de number of API and it will be called and the result will be printed in the screen.

```python
>>> import adroc_test.test as test
>>> test.menu()
Choose 0=Exit 1-BA, 2-OSA: 1
1
List of function:
1 get_customer_subscription_list
2 get_domain
3 get_last_to_serv_status_transition_date
4 get_order
5 get_order_by_status
6 get_order_fin_details_list
7 get_plan_category_details
8 get_plan_category_list
9 get_plan_details
10 get_plan_period_list
11 get_rate_full_list
12 get_sales_order_by_subsctiption
13 get_subscription
14 get_subscription_extended
15 get_subscription_list_by_order
16 get_subscription_param_value
17 get_subscription_private
18 get_subsctiption_by_resource_list
19 get_subsctiption_resources_list
20 send_notification
Choose one function: 2
{'AccountID': 1000001, 'VendorID': 1, 'DomainID': 914, 'FullDomainName': 'huawei.net', 'DomainZoneID': 'net', 'Status': 'Canceled', 'External DNS': 'external DNS', 'RegistrationPeriod': 1, 'startDate': datetime.datetime(2019, 4, 10, 16, 25, 9), 'ExpirationDate': datetime.datetime(2019, 5, 10, 0, 0), 'PrimaryNameServer': 'lindns01.lab.com.br', 'SecondaryNameServer': 'lindns02.lab.com.br', 'ThirdNameServer': '', 'FourthNameSever': '', 'CompanyName': 'UAT', 'FName': 'Emerson', 'MName': '', 'LName': 'Silva', 'Email': '2019@gmail.com', 'getPhone': '+55(11)12345678', 'getFax': ''}
Choose 0=Exit 1-BA, 2-OSA:
```

#### 2.Unit Test

In the folder `tests` are the files that allow you to test all methods.
Copy the template file `adroc_test/test_config.py.template` to `adroc_test/test_config.py` and fill it with your Odin data.
Use de Python Unit Text comand in the root folder:
```
python -m unittest
```

If every thing is OK, you will see this message:
```
.......................
----------------------------------------------------------------------
Ran 23 tests in 2.395s

OK
```

### Usage

```python
from odin.wrapper.proxy import BssCaller
from odin.wrapper.proxy import OssCaller
from odin.api.bss import Bss 
from odin.api.oss import Oss 

# For BA (BSS)
bss_caller = BssCaller(bss_server_url)
bss = Bss(bss_caller)

# For OSA (OSS)
oss_caller = OssCaller(oss_server_url)
oss = Oss(oss_caller)

# Calling OSS
result = oss.get_subscription_token(account_id, subscription_id)
print(result)

# Calling BSS
result = bss.get_subscription(subscription_id)
print(result)
```

### Important
I just had implemented the API calls that was need in my project. If you need more, please implement it.

There are no authentication, as we do not use token. All you need to do is allow your netowork or IP adreess in the Operation Panel:

`Settings > Plublic API > Allowed Networks`

Click in the buttom `Add` and add you IP or network.

