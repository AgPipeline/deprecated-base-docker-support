"""Tests for 'transformer_class.py"
"""

#Import transformer_class.py module and inmedded modules
from transformer_class import Transformer
import argparse

#Initial testing values
test_transformer = Transformer()
parse = argparse.ArgumentParser(description='Test')
test_metadata = {}

def test_add_parameters():
    """Test for add_parameters function
    """
    #Saving method call to variable
    testee = test_transformer.add_parameters(parse)
    #Should return None
    assert testee == None
    
def test_transformer_params():
    """Test for transformer params
    """
    #Saving method call to variable
    testee = test_transformer.get_transformer_params(parse, test_metadata)
    #Should return dict type
    assert isinstance(testee, dict)