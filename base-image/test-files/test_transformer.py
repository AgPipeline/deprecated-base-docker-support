"""Tests for transformer.py
"""

# Import transformer.py module and imbedded modules
import argparse
import transformer
from transformer_class import Transformer

# Initial testing values
TEST_TRANSFORMER = Transformer()
PARSE = argparse.ArgumentParser()


# pylint: disable=assignment-from-no-return
def test_add_parameters():
    """Testing add_parameters function
    """
    # Saving function call to variable
    testee = transformer.add_parameters(TEST_TRANSFORMER)
    # Should return None
    assert testee is None


def test_check_continue():
    """Testing check_continue function
    """
    # Saving function call to variable
    testee = transformer.check_continue(TEST_TRANSFORMER)
    # Should return dict type
    assert isinstance(testee, dict)


def test_perform_process():
    """Test of the perform_process function
    """
    # Storing function call to a variable
    testee = transformer.perform_process(TEST_TRANSFORMER)
    # Should return dict type
    assert isinstance(testee, dict)
