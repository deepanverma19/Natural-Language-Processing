# CS 6320 - Natural Language Processing
# Group Project
#
# Task 1:
#       Create a corpus of news articles
#
# Authors:
#       Stephen Blystone (smb032100@utdallas.edu)
#       Amit Gupta (axg162930@utdallas.edu)
#       Deepan Verma (dxv160430@utdallas.edu)
#
# Teamname:
#       GASBDV (General Anakin Skywalker Becomes Darth Vader)
import os
import sys
import argparse

# For Testing Purposes.
### DO NOT MAKE CHANGES TO TESTING VARIABLE HERE ###
### ONLY MAKE CHANGES FROM COMMAND-LINE OPTIONS ###
DEBUG = False  # True/False.

# Get directory of executable files are located in relative to python file.
execDir = os.path.dirname(os.path.realpath(__file__))


def printDebugMsg(text):
    """Used for printing debug messages."""
    if DEBUG:
        print(text)


def runAlgorithm(args):
    """Main function that runs the Algorithm"""
    # Parse arguments
    parser = argparse.ArgumentParser(description='Template (CHANGE THIS FOR SPECIFIC TASK)')
    parser.add_argument('--debug', required=False, action="store_true",
                        help="Enable to print Debug Messages.")
    args = parser.parse_args()

    # Set global debug flag.
    if args.debug:
        global DEBUG
        DEBUG = True

    # Finished parsing command-line options.
    printDebugMsg("Finished with argument parsing.")


if __name__ == "__main__":
    runAlgorithm(sys.argv[1:])
