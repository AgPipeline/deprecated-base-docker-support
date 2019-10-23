"""Class instance for Transformer
"""

import argparse

#pylint: disable=unused-argument
class Transformer():
    """Generic class for supporting transformers
    """
    def __init__(self):
        """Performs initialization of class instance
        """

    def add_parameters(self, parser: argparse.ArgumentParser) -> None:
        """Adds processing parameters to existing parameters
        Arguments:
            parser: instance of argparse
        """

    #pylint: disable=no-self-use
    def get_transformer_params(self, args: argparse.Namespace, metadata: dict) -> dict:
        """Returns a parameter list for processing data
        Arguments:
            args: result of calling argparse.parse_args
            metadata: the loaded metadata
        """
        params = {}
        return params
