"""Tests for transformer.py
"""

#Import testing module
import unittest

#Import transformer_class.py module and inbedded modules
import transformer
import transformer_class
import argparse


#Create testing class
class TransformerTest(unittest.TestCase):
    """Generic Class for running tests
    """
    def setUp(self):
        """Sets up an initial instance of the transformer class
        """
        self.transformer = transformer_class.Transformer()

    def test_add_parameters(self):
        """
        Testing add_parameters function
        """
        #create an argparse instance
        parse = argparse.ArgumentParser(description= "Test")
        
        #Checks that add_parameters returns None
        testee =transformer.add_parameters(parse) 
        self.assertIsNone(testee, 'Does not return None')
        

    def test_check_continue(self):
        """Testing check_continue function
        """
        
        #Storing function call to a variable
        testee = transformer.check_continue(self.transformer)
        self.assertIsInstance(testee, dict, "Should return dict type")

    def test_perform_process(self):
        """Test of the perform_process function
        """
        
        #storing function call to variable
        testee = transformer.perform_process(self.transformer)
        self.assertIsInstance(testee, dict, "Should return dictionary type")
        
        
        




    
