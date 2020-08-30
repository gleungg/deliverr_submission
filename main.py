#!/usr/bin/env python
# coding: utf-8

from collections import defaultdict

class Solution:
    '''
    Because we are guaranteed that the warehouses come in order of shipping 
    cost, we can utilize a greedy approach to solve this problem.
    
    1. For each order item, go through each warehouse from cheapest to most expensive
    trying to fulfil the order. If unable to do so, immediately return empty list
    
    2. We need to constantly update the dictionary throughout the process in order
    to ensure taht we are not overriding any information
    
    '''
    def minimizeOrderCost(order, warehouse):
        res = []
        dictionary = defaultdict(dict)
        for key, value in order.items():
            index = 0
            counter = 0
            curr_level = defaultdict(dict)
            while value > 0 and index < len(warehouse):
                if key in warehouse[index]["inventory"]:
                    in_stock = min(warehouse[index]["inventory"][key], value)
                    value -= in_stock
                    warehouse[index]["inventory"][key] -= in_stock
                    counter += in_stock
                    curr_level[warehouse[index]['name']][key] = in_stock
                index += 1

            if value == 0: 
                ## Process results 
                for key, value in curr_level.items():
                    dictionary[key].update(value)
            else:
                return []
        for key, value in dictionary.items():
            res.append({key:value})

        return res