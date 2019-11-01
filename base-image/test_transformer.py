"""Tests for transformer.py
"""

#Import transformer.py module and imbedded modules
import transformer
from transformer_class import Transformer
import argparse

#Initial testing values
test_transformer = Transformer()
parse = argparse.ArgumentParser()

def test_add_parameters():
    """Testing add_parameters function
    """
    #Saving function call to variable
    testee = transformer.add_parameters(test_transformer)
    #Should return None
    assert testee == None

def test_check_continue():
    """Testing check_continue function
    """
    #Saving function call to variable
    testee = transformer.check_continue(test_transformer)
    #Should return dict type
    assert isinstance(testee, dict)

def test_perform_process():
    """Test of the perform_process function
    """
    #Storing function call to a variable
    testee = transformer.perform_process(test_transformer)
    #Should return dict type
    assert isinstance(testee, dict)