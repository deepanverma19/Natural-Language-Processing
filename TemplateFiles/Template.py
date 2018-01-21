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
### DO NOT MAKE CHANGES TO TESTING VARIABLES HERE ###
# ONLY MAKE CHANGES FROM COMMAND-LINE OPTIONS
DEBUG = False  # True/False.
# DEBUGLVL 1 indicates print all DEBUG messages.
# Higher numbers are more restrictive.
DEBUGLVL = 1

# Get directory of executable files are located in relative to python file.
execDir = os.path.dirname(os.path.realpath(__file__))


def printDebugMsg(text, level=1):
    """Used for printing debug messages.
    Only print if:
        1) DEBUG flag set to True
        2) level of debug message is >= DEBUGLVL.

    Example:
        DEBUGLVL = 3
        printDebugMsg("Test")  # Defaults to level 1
        printDebugMsg("Test2", 2)
        printDebugMsg("Test3", 3)
        printDebugMsg("Test5", 5)

        The above would output the following since DEBUGLVL = 3:
            Test3
            Test5
    """
    if DEBUG:
        if level >= DEBUGLVL:
            print(text)


def runAlgorithm(args):
    """Main function that runs the Algorithm"""
    # Parse arguments
    parser = argparse.ArgumentParser(description='Template (CHANGE THIS FOR SPECIFIC TASK)')
    parser.add_argument('--debug', required=False, action="store_true",
                        help="Enable to print Debug Messages.")
    parser.add_argument('--debuglvl', required=False, default=1,
                        help="Specify level of debug messages to print. Default is 1")
    args = parser.parse_args()

    # Check that if debuglvl flag set, that debug flag also set.
    if args.debuglvl and not args.debug:
        print("ERROR: --debuglvl flag set but --debug flag NOT set.")
        print("Please re-run with --debug flag set.")
        sys.exit(1)

    # Set global debug flag.
    if args.debug:
        global DEBUG
        DEBUG = True

    # Set global debug level flag.
    if args.debuglvl:
        # Check that value entered is an integer.
        try:
            global DEBUGLVL
            DEBUGLVL = int(args.debuglvl)
        except:
            print("ERROR: Debuglvl is not an integer. Please try again with input as an integer.")
            sys.exit(1)

    # Finished parsing command-line options.
    printDebugMsg("Finished with argument parsing.")


if __name__ == "__main__":
    runAlgorithm(sys.argv[1:])
