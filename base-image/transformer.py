"""Testing instance of transformer
"""

import argparse
import transformer_class

#pylint: disable=unused-argument
def add_parameters(parser: argparse.ArgumentParser) -> None:
    """Adds parameters
    Arguments:
        parser: instance of argparse
    """

def check_continue(transformer: transformer_class.Transformer) -> dict:
    """Checks if conditions are right for continuing processing
    Arguments:
        transformer: instance of transformer class
    Return:
        Returns a dictionary containining the return code for contiuing or not, and
        an error message
    """
    return {'code': 0}

def perform_process(transformer: transformer_class.Transformer) -> dict:
    """Performs the processing of the data
    Arguments:
        transformer: instance of transformer class
    Return:
        Returns a dictionary with the results of processing
    """
    return {'code': 0, 'message': "Everything is going swimmingly"}
