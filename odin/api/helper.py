from datetime import datetime
import time
import calendar

def datetime2timestamp(date : datetime):
    """
    Convert datetime to unix timestamp
    :param date: Date to be converted in a unix timestamp
    :type date: datetime
    
    :return: Unix timestamp
    :rtype: int
    """
    return int(time.mktime(date.timetuple()))

def timestamp2datetime(unixtime : float):
    """
    Convert unix timestamp to datetime
    :param unixtime: Unix timestamp to be converted in a datetime
    :type unixtime: int
    
    :return: datetime
    :rtype: datetime
    """
    if unixtime and unixtime > 0:
        result = datetime.fromtimestamp(unixtime)
    else:
        result = None
    return result

def datetime_month_fistday( date : datetime ):
    """
    Get the first day of the month at 00:00:00.000
    :param date: Date
    :type date: datetime
    
    :return: The date setted with the first day of month
    :rtype: datetime
    """
    return date.replace(day=1, hour = 0, minute = 0, second=0, microsecond=0 )

def datetime_month_lastday( date : datetime ):
    """
    Get the last day of the month at 23:59:59.999999
    :param date: Date
    :type date: datetime
    
    :return: The date setted with the last day of month
    :rtype: datetime
    """
    last_day = calendar.monthrange(date.year,date.month)[1]
    return date.replace(day = last_day, hour = 23, minute = 59, second=59, microsecond=999999 )