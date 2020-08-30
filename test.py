#!/usr/bin/env python
# coding: utf-8
'''
Prior to writing and testing code, decisions should always be made in terms of "how" we test the code. 
For example, two outputs for orders may be identical, except for the order it is listed in 
'''

import unittest
from main import Solution as main

class TestStringMethods(unittest.TestCase):
    
    ## One warehouse with perfect inventory should output a proper list
    def test_oneWarehouse_perfectInventory(self):
        order = {"apple":1, "banana":1, "cucumber":1, "mango":1, "pineapple":1}
        warehouse = [{"name":"warehouse", "inventory":{"apple":1, "banana":1, "cucumber":1, "mango":1, "pineapple":1}}]
        output = [{"warehouse":{"apple":1, "banana":1, "cucumber":1, "mango":1, "pineapple":1}}]
        self.assertEqual(output, main.minimizeOrderCost(order, warehouse))

     
    ## One warehouse with more than sufficient inventory should output a proper list   
    def test_oneWarehouse_extraInventory(self):
        order = {"apple":10, "banana":5, "cucumber":6, "mango":6, "pineapple":2}
        warehouse = [{"name":"warehouse", "inventory":{"apple":15, "banana":12, "cucumber":13, "mango":13, "pineapple":10}}]
        output = [{"warehouse":{"apple":10, "banana":5, "cucumber":6, "mango":6, "pineapple":2}}]
        self.assertEqual(output, main.minimizeOrderCost(order, warehouse))
        
    ## If a warehouse doesn't have sufficient inventory, we should output an empty list
    def test_oneWarehouse_badInventory(self):
        order = {"apple":2, "banana":2, "cucumber":2, "mango":2, "pineapple":2}
        warehouse = [{"name":"warehouse", "inventory":{"apple":1, "banana":1, "cucumber":1, "mango":1, "pineapple":1}}]
        output = []
        self.assertEqual(output, main.minimizeOrderCost(order, warehouse))
        
    ## Testing to ensure that we have proper output when there are two warehouses
    def test_twoWarehouse_perfectInventory(self):
        order = {"apple":10, "banana":10, "cucumber":10, "mango":10, "pineapple":10}
        warehouse = [{"name":"warehouse", "inventory":{"apple":5, "banana":5, "cucumber":5, "mango":5, "pineapple":5}}, 
                    {"name":"factory", "inventory":{"apple":5, "banana":5, "cucumber":5, "mango":5, "pineapple":5}}]
        output = [{"warehouse":{"apple":5, "banana":5, "cucumber":5, "mango":5, "pineapple":5}}, 
                 {"factory":{"apple":5, "banana":5, "cucumber":5, "mango":5, "pineapple":5}}]
        self.assertEqual(output, main.minimizeOrderCost(order, warehouse))

    ## Ensure output empty if inventory insufficient for multiple warehouses 
    def test_twoWarehouse_badInventory(self):
        order = {"apple":10, "pear":10, "peach":10}
        warehouse = [{"name":"warehouse", "inventory":{"apple":5, "banana":5, "cucumber":5, "mango":5, "pineapple":5}}, 
                    {"name":"factory", "inventory":{"apple":5, "banana":5, "cucumber":5, "mango":5, "pineapple":5}}]
        output = []
        self.assertEqual(output, main.minimizeOrderCost(order, warehouse))
        
    ## If multiple factories satisfy the order, we should output based on minimal cost
    def test_shippingOrder(self):
        order = {"apple":10}
        warehouse = [{"name":"factory", "inventory":{"apple":15}},
             { "name": "warehouse","inventory":{"apple": 15}}]
        output = [{"factory":{"apple":10}}]
        self.assertEqual(output, main.minimizeOrderCost(order, warehouse))
        
    ## Even if the warehouse can fulfil the entire order, we want the factory to handle as much of the order as possible to minimize cost
    def test_shippingCost(self):
        order = {"apple":10}
        warehouse = [{"name":"factory", "inventory":{"apple":9}},
             { "name": "warehouse","inventory":{"apple": 15}}]
        output = [{"factory":{"apple":9}}, {"warehouse":{"apple":1}}]
        self.assertEqual(output, main.minimizeOrderCost(order, warehouse))

    if __name__ == "__main__":
        unittest.main(argv=["first-arg-is-ignored"], exit=False)