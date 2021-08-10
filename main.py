#! /usr/bin/env python3
import argparse 
import logging
import time
from pyopenms import *
import os
import sys


def timing(f):
    """
    Helper function for timing other functions

    Parameters
    ----------
    f : function

    Returns
    -------
    function: new function wrap with timer and logging 
    """
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        logging.info('{:s} function took {:.3f} s'.format(f.__name__, (time2-time1)))
        return ret
    
    return wrap


def process_arg(args):
    """
    Convert namespace args objet to dictionary.

    Helper function. conversion of the args from namespace to dictionary
    allows for easier passing and modification.

    Parameters
    ----------
    args : args manespace object from argspars

    Returns
    -------
    dict : dictionary of arguments
    """
    return vars(args)


@timing
def run(kwargs):
    print(kwargs)
    """
    Parameters
    ----------
    args : 
    kwargs:

    Returns
    -------
    None
    """


    logging.info("Starting")
    

    logging.info("Done")


def main():
    """
    Main Function

    Parse arguments and start writing

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    # Argument Parser
    parser = argparse.ArgumentParser(description="tdf2mzml")

    parser.add_argument(
        '-in',
        '--input',
        required=True,
        help='Input File')

    parser.add_argument(
        '-out',
        '--output',
        required=True,
        help='Output File')
    
    parser.add_argument(
        '-np',
        '--number_of_processes',
        help='Number of processes',
        default=1)

    parser.add_argument(
        '--debug',
        action='store_true',
        help='Enable debugging output')

    logging.basicConfig(level=logging.INFO)

    args = process_arg(parser.parse_args())

    run(args)


if __name__ == "__main__":
    
    main()
