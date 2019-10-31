"""Tests for 'entrypoint.py'
"""

#Importing testing package
import unittest

#Import entrypoint.py and embedded modules
from entrypoint import __internal__, add_parameters,do_work
import argparse
import os
import json
import logging
import transformer_class
import configuration
import transformer

#Create testing class
class EntrypointTest(unittest.TestCase):
    """Generic class for running tests
    """
    def setUp(self):
        """Sets up initial instance of __internal__ class
        """
        self.internal = __internal__()
        self.transformer = transformer_class.Transformer()

    def test_handle_error(self):
        """Test for handle_error method
        """
        
        #Setting up testing arguments
        test_code = 117
        test_message = "Test message"

        #Initial test using "ideal" args
        ideal_example = self.internal.handle_error(test_code,test_message)
        self.assertIsInstance(ideal_example, dict, "Should return a dict type")

        #Secondary tests
        test_code = None
        test_message = False

        secondary_example = self.internal.handle_error(test_code, test_message)
        self.assertIsInstance(secondary_example, dict, "Should return a dict type")

    def test_load_metadata(self):
        """Test the load_metadata method
        """
        
        #setting up testing argument(s)
        test_path = "https://example-metadata-path.com"
        
        #Test
        testee = self.internal.load_metadata(test_path)
        self.assertIsInstance(testee, dict, 'Should return a dict type')
        

    def test_parse_continue_result(self):
        """Test of the parse_continue_resilt method
        """

        #Saving check_continue result to variable
        test_result = transformer.check_continue(self.transformer)

        #Assigning method to variable
        continue_result = self.internal.parse_continue_result(test_result)

        #Making sure it returns a list
        self.assertIsInstance(continue_result, list, "Should return a list")

    def test_handle_check_continue(self):
        """Test for handle_check_continue
        """

        #Setting up a test dictionary
        test_dict = {"Test": 0}

        #Saving method call to a variable
        check_handle = self.internal.handle_check_continue(self.transformer,test_dict)

        #Checking output type
        self.assertIsInstance(check_handle, dict,\
             "Should return a dictionary")

    def test_perform_processing(self):
        """Test of the perform_processing method
        """

        #Create an argparse instance
        parse = argparse.ArgumentParser()

        #Create a test metadata dictionary
        test_metadata = {}

        #Store perform_processing call to variable
        test_processing = self.internal.perform_processing(self.transformer,parse, test_metadata)

        #Check that return is a dict type
        self.assertIsInstance(test_processing, dict, "Should be dict type")


    def test_handle_result(self):
        """Test for handle_result method
        """

        #Create variables for arguments
        test_types = 'print'
        
        test_path = '\base-docker-support\base-image'
        test_result = {}

        #saving method call to vaiable
        handled_result = self.internal.handle_result(test_types,test_path, test_result)

        #Testing output type
        self.assertIsInstance(handled_result, dict, "Should return dict type")

        #Testing that the method returns the test_result parameter
        self.assertEqual(handled_result, test_result, "Should return third parameter unchanged")

    def test_add_parameters(self):
        """Testing add_parameters function
        """

        #Create a test argparse instance
        parse = argparse.ArgumentParser()

        #Save function to a variable
        added_params = add_parameters(parse, self.transformer)

        #Checking it returns None
        self.assertIsNone(added_params, "Function should return None")

    def test_do_work(self):
        """Test for do_work function
        """

        #Create argparse instance
        parse = argparse.ArgumentParser()

        #Store function call to a variable
        done_work = do_work(parse)
        
        #Check that the function returns None
        self.assertIsNone(done_work, "Function should return None")