"""
The UQCS Committee orders pizza for most of their events. Unfortunately, someone messed up and now all the orders are jumbled! The orders are stored as an array (list) comprised of strings which have a date and the number of pizzas ordered on that date. The treasurer needs the pizza orders to be sorted from the oldest order to the newest so that it can be added to the ledger easily! Help the treasurer solve this: return an array (list) where the pizza orders are sorted in ascending order (oldest first).

Input Format: Array (list) of strings, where each string is of the format date num_pizzas.
Date in each string is formatted as MM-DD-YYYY.

Constraints: Array (list) is of size , where 

Output Format: Array (list) of strings, sorted with oldest orders first.
"""

import math
import os
import random
import re
import sys
from datetime import datetime

orders = ['10-28-2013 53', '05-24-2017 41', '06-06-2013 40', '10-20-2019 18', '06-15-2016 44', '02-07-2012 59']

def sort_pizza_orders(orders):
    """
    Sort unorded array of strings with order date and number of pizzas.

    param: 
        orders(arr): Strings with format 'MM-DD-YYYY ##'

    return:
        array: Strings in desc chronological order

    """
    # Split each entry in orders into tuples
    order_tuple = [tuple(map(str, i.split())) for i in orders] 
    # Create a dictionary with the date as key and number of pizzas as value
    order_dict = dict(order_tuple)
    # Convert date into 'datetime' type & sort dict using date in reverse order
    ordered_data = sorted(order_dict.items(), 
        key = lambda x:datetime.strptime(x[0], '%m-%d-%Y'), reverse=False)

    # Change dictionary back into string
    sorted_orders = [' '.join(tups) for tups in ordered_data]
    return(sorted_orders)
    
# Run sample
sample = sort_pizza_orders(orders)
mystring = '\n'.join(sample)
print(mystring)

