#!/usr/bin/env python3
"""Base entry point for Agriculture Pipeline transformer
"""

import argparse
import os
import json
import logging

import transformer_class

# From derived images
import configuration
import transformer

# Setup where sensor data is location in this image
#terrautils.lemnatec.SENSOR_METADATA_CACHE = os.path.dirname(os.path.realpath(__file__))

class __internal__():
    """Class for functions intended for internal use only for this file
    """
    def __init__(self):
        """Performs initialization of class instance
        """

    @staticmethod
    def handle_error(code: int, message: str) -> dict:
        """Handles logging and return values when an error ocurrs. Implies processing
           will stop.
        Arguments:
            code: return code related to the error
            message: the message string of the error
        Return:
            Returns a dict with the code and message
        """
        if code is None:
            logging.warning("An error has occurred without a return code specified, setting default return code")
            code = -1
        if not message:
            logging.warning("An error has occurred without a message, setting default message")
            message = "An error has ocurred with error code (%s)" % str(code)

        logging.error(message)
        logging.error("Stopping processing")

        result = {}
        result['error'] = message
        result['code'] = code

        return result

    @staticmethod
    def load_metadata(metadata_path: str) -> dict:
        """Loads the metadata from the specified path
        Arguments:
            metadata_path: path to the metadata file
        Return:
            Returns a dict containing the loaded metadata. If an error ocurrs, the dict
            won't contain metadata but will contain an error message under an 'error' key.
        """
        try:
            with open(metadata_path, 'r') as in_file:
                md_load = json.load(in_file)
                if not md_load is None:
                    md_return = {'metadata': md_load}
                else:
                    msg = 'Invalid JSON specified in metadata file "%s"' % metadata_path
                    logging.error(msg)
                    md_return = {'error': msg}
        except Exception as ex:
            msg = 'Unable to load metadata file "%s"' % metadata_path
            logging.error(msg)
            logging.error('Exception caught: %s', str(ex))
            md_return = {'error': msg}

        return md_return

    @staticmethod
    def parse_continue_result(result) -> list:
        """Parses the result of calling transformer.check_continue and returns
           the code and/or message
        Arguments:
            result: the result from calling transformer.check_continue
        Return:
            A list containing the result code and result message. One or both of these
            values in the list may be None
        """
        result_code = None
        result_message = None

        if isinstance(result, int):
            result_code = result
        elif not isinstance(result, str):
            result_len = len(result)
            if result_len > 0:
                result_code = result[0]
            if result_len > 1:
                result_message = result[1]

        return (result_code, result_message)

    @staticmethod
    def handle_check_continue(transformer_instance: transformer_class.Transformer, transformer_params: dict) -> dict:
        """Handles calling the transformer.check_continue function
        Arguments:
            transformer_instance: instance of Transformer class
            transformer_params: dictionary of parameters to pass to transform module functions
        Return:
            Returns the result of checking to continue operation
        """
        result = {}

        if hasattr(transformer, 'check_continue'):
            check_result = transformer.check_continue(transformer_instance, **transformer_params)
            result_code, result_message = __internal__.parse_continue_result(check_result)

            if result_code:
                result['code'] = result_code
            if result_message:
                result['message'] = result_message
        else:
            logging.debug("transformer module doesn't have a function named 'check_continue'")

        return result

    @staticmethod
    def perform_processing(transformer_instance, args: argparse.ArgumentParser, metadata: dict) -> dict:
        """Makes the calls to perform the processing
        Arguments:
            transformer_instance: instance of transformer class
            args: the command line arguments
            metadata: the loaded metadata
        Return:
            Returns a dict containing the result of processing
        """
        result = {}

        # Get the various types of parameters from the transformer instance
        if hasattr(transformer_instance, 'get_transformer_params'):
            transformer_params = transformer_instance.get_transformer_params(args, metadata)
            if not isinstance(transformer_params, dict):
                return __internal__.handle_error(-101, \
                    "Invalid return from getting transformer parameters from transformer class instance")
        else:
            logging.debug("Transformer class instance does not have get_transformer_params method")
            transformer_params = {}

        # First check if the transformer thinks everything is in place
        if hasattr(transformer, 'check_continue'):
            result = __internal__.handle_check_continue(transformer_instance, transformer_params)
            if 'code' in result and result['code'] < 0 and 'error' not in result:
                result['error'] = "Unknown error returned from check_continue call"
        else:
            logging.debug("transformer module doesn't have a function named 'check_continue'")

        # Next make the call to perform the processing
        if not 'error' in result:
            if hasattr(transformer, 'perform_process'):
                result = transformer.perform_process(transformer_instance, **transformer_params)
            else:
                logging.debug("transformer module is missing function named 'perform_process'")
                return __internal__.handle_error(-102, "Transformer perform_process interface is not available " +
                                                 "for processing data")

        return result

    @staticmethod
    def handle_result(result_types: str, result_file_path: str, result: dict) -> None:
        """Handles the results of processing as dictated by the arguments passed in.
        Arguments:
            result_types: comma separated string containing one or more of: all, file, print
            result_file_path: location to place result file
            result: the dictionary of result information
        Return:
            Returns the result parameter
        Notes:
            If result_types is None then no actions are taken. If 'file' or 'all' is specified
            in result_types and result_file_path is None or empty, writing to a file is skipped
        """
        if not result_types is None:
            type_parts = [one_type.strip() for one_type in result_types.split(',')]
            if 'print' in type_parts or 'all' in type_parts:
                print(json.dumps(dict, indent=2))
            if 'file' in type_parts or 'all' in type_parts:
                if result_file_path:
                    os.makedirs(result_file_path, exist_ok=True)
                    with open(result_file_path, 'w') as out_file:
                        json.dump(result, out_file, indent=2)
                else:
                    logging.warning("Writing result to a file was requested but a file path wasn't provided.")
                    logging.warning("    Skipping writing to a file.")

        return result

def add_parameters(parser: argparse.ArgumentParser, transformer_instance) -> None:
    """Function to prepare and execute work unit
    Arguments:
        parser: an instance of argparse.ArgumentParser
    """
    parser.add_argument('--debug', '-d', action='store_const',
                        default=logging.WARN, const=logging.DEBUG,
                        help='enable debug logging (default=WARN)')

    parser.add_argument('--info', '-i', action='store_const',
                        default=logging.WARN, const=logging.INFO,
                        help='enable info logging (default=WARN)')

    parser.add_argument('--result', nargs='?', default='all',
                        help='Direct the result of a run to one or more of (all is default): "all,file,print"')

    parser.add_argument('--metadata', default=None,
                        help='The path to the source metadata')

    parser.add_argument('working_space', type=str, help='the folder to use use as a workspace and for storing results')

    # Let the transformer class add parameters
    if hasattr(transformer_instance, 'add_parameters'):
        transformer_instance.add_parameters(parser)

    # Check if the transformer has a function defined to extend command line arguments
    if hasattr(transformer, 'add_parameters'):
        transformer.add_parameters(parser)

def do_work(parser: argparse.ArgumentParser) -> None:
    """Function to prepare and execute work unit
    Arguments:
        parser: an instance of argparse.ArgumentParser
    """
    result = {}

    # Create an instance of the transformer
    transformer_instance = transformer_class.Transformer()
    if not transformer_instance:
        result = __internal__.handle_error(-100, "Unable to create transformer class instance for processing")
        return __internal__.handle_result(None, None, result)

    add_parameters(parser, transformer_instance)
    args = parser.parse_args()

    # start logging system
    logging.getLogger().setLevel(args.debug if args.debug == logging.DEBUG else args.info)

    # Check that we have mandatory metadata
    if not args.metadata:
        result = __internal__.handle_error(-1, "No metadata path was specified.")
    elif not os.path.exists(args.metadata):
        result = __internal__.handle_error(-2, "Unable to access metadata file '%s'" % args.metadata)
    else:
        md_result = __internal__.load_metadata(args.metadata)
        if 'metadata' in md_result:
            result = __internal__.perform_processing(transformer_instance, args, md_result)
        else:
            result = __internal__.handle_error(-3, md_result['error'])

    __internal__.handle_result(args.result, os.path.join(args.working_space, 'result.json'), result)
    return result

if __name__ == "__main__":
    try:
        PARSER = argparse.ArgumentParser(description=configuration.DESCRIPTION)
        do_work(PARSER)
    except Exception as ex:
        logging.error("Top level exception handler caught an exception: %s", str(ex))
        raise
