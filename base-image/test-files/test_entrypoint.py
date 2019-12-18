"""Tests for 'entrypoint.py'
"""

#Import entrypoint.py and embedded modules
import argparse
import entrypoint                         # @UnusedImport
import transformer                        # @UnusedImport
from transformer_class import Transformer  # @UnusedImport

#Set up initial testing values
TEST_TRANSFORMER = Transformer()
PARSE = argparse.ArgumentParser(description="test")
TEST_INTERNAL = entrypoint.__internal__()

def test_handle_error():
    """Test for handle error
    """
    #Some testing arguments
    test_code = 117
    test_message = "Test message"

    #Initial test using "ideal" args
    ideal_example = TEST_INTERNAL.handle_error(test_code, test_message)
    #Should return dict type
    assert isinstance(ideal_example, dict)

    #A secondary test
    test_code = None
    test_message = False

    secondary_example = TEST_INTERNAL.handle_error(test_code, test_message)
    assert isinstance(secondary_example, dict)

def test_load_metadata():
    """Test load_metadata method
    """

    #Set some testing arguments
    test_path = "https://example-metadata-path.com"

    #Save method call to variable
    testee = TEST_INTERNAL.load_metadata(test_path)
    #Should return dict type
    assert isinstance(testee, dict)

def test_parse_continue_result():
    """Test of the parse_continue method
    """

    #Saving check_continue result to a variable
    check_result = transformer.check_continue(TEST_TRANSFORMER)
    #Assigning method call to variable
    continue_result = TEST_INTERNAL.parse_continue_result(check_result)
    #Should return list type
    assert isinstance(continue_result, tuple)

def test_handle_check_continue():
    """Test for handle_check_continue method
    """

    #Creating a testing dictionary
    test_dict = {}
    
    #Saving method call to variable
    testee = TEST_INTERNAL.handle_check_continue(TEST_TRANSFORMER, test_dict)

    #Should return dict type
    assert isinstance(testee, dict)

def test_perform_processing():
    """Test for perform_processing method
    """

    #Call the load_metadata method and store result to a variable
    test_path = "https://example-metadata-path.com"
    test_metadata = TEST_INTERNAL.load_metadata(test_path)

    #Save method call to variable
    test_process = TEST_INTERNAL.perform_processing(TEST_TRANSFORMER, PARSE, test_metadata)

    #Should return dict
    assert isinstance(test_process, dict)


def test_handle_result():
    """Test for handle_result method
    """

    #Set up testing variables
    test_result_str = "all,file,print"
    test_path = "~/Documents"
    test_dict = {}

    #Store function call to variable
    test_handl_res = TEST_INTERNAL.handle_result(test_result_str, test_path, test_dict)

    #Should return the test_dict
    assert test_handl_res == test_dict



def test_add_parameters():
    """Test add_parameters function
    """

    #Save function call to variable
    test_params = entrypoint.add_parameters(PARSE, TEST_TRANSFORMER)

    #Should return None
    assert test_params is None

def test_do_work():
    """Test for do_work function
    """
    
    #Save function call to variable
    test_work = entrypoint.do_work(PARSE)

    #Should return None
    assert test_work is None
