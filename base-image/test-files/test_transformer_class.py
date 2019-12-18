"""Tests for 'transformer_class.py"
"""

#Import transformer_class.py module and inmedded modules
import argparse
from transformer_class import Transformer  # @UnusedImport

#Initial testing values
TEST_TRANSFORMER = Transformer()
PARSE = argparse.ArgumentParser(description='Test')
TEST_METADATA = {}

def test_add_parameters():
    """Test for add_parameters function
    """
    #Saving method call to variable
    testee = TEST_TRANSFORMER.add_parameters(PARSE)
    #Should return None
    assert testee is None
    
def test_transformer_params():
    """Test for transformer params
    """
    #Saving method call to variable
    testee = TEST_TRANSFORMER.get_transformer_params(PARSE, TEST_METADATA)
    #Should return dict type
    assert isinstance(testee, dict)
