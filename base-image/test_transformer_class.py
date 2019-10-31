"""Tests for 'transformer_class.py"
"""

#Import testing module
import unittest

#Import transformer_class.py module and inbedded modules
from transformer_class import Transformer
import argparse


#Create testing class
class TransformerClassTest(unittest.TestCase):
    """Generic Class for running tests
    """
    def setUp(self):
        """Sets up an initial instance of the class
        """
        self.transformer = Transformer()

    def test_add_parameters(self):
        """
        Testing add_parameters method
        """
        #create an argparse instance
        parse = argparse.ArgumentParser(description= "Test")
        
        #Checks that add_parameters returns None
        self.assertIsNone(self.transformer.add_parameters(parse),\
            'Does not return None')
        
        #Similar only stored in a variable
        testee = self.transformer.add_parameters(parse)
        self.assertIsNone(testee, "")



    def test_get_transformer_params(self):
        """Testing transformer_params method
        """
        #create an argparse.Namespace instance
        parse = argparse.Namespace
        #create test dictionary
        test_data = {}
        
        #Tests to make sure return value is dict type
        self.assertIsInstance(self.transformer.get_transformer_params(parse,test_data), dict, \
            "Did not return a dictionary object type")
        
        #Similar only stored in a vaiable
        testee = self.transformer.get_transformer_params(parse,test_data)
        self.assertIsInstance(testee, dict, "Not a dictionary")
        
        
        




    
