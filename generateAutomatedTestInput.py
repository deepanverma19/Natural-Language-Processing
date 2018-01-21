# CS 6320 - Natural Language Processing
# Group Project
#
# Helper Function for Task 4
#
# Authors:
#       Stephen Blystone (smb032100@utdallas.edu)
#       Amit Gupta (axg162930@utdallas.edu)
#       Deepan Verma (dxv160430@utdallas.edu)
#
# Teamname:
#       GASBDV (General Anakin Skywalker Becomes Darth Vader)

import os
import argparse
import datetime

# For Testing Purposes.
### DO NOT MAKE CHANGES TO TESTING VARIABLE HERE ###
### ONLY MAKE CHANGES FROM COMMAND-LINE OPTIONS ###
DEBUG = False  # True/False.

# Get directory of executable files are located in relative to python file.
execDir = os.path.dirname(os.path.realpath(__file__))


def printDebugMsg(text):
    """Used for printing debug messages."""
    global DEBUG
    if DEBUG:
        print(text)


# listOfParameters = ["SENTENCE", "LEMMA", "STEM", "POSTAG",
#                     "HEADWORD", "HYPERNYM", "HYPONYM", "MERONYM", "HOLONYM"]
#
# listOfFlags = ["{}_FLAG".format(x) for x in listOfParameters]
# listOfWeights = ["{}_WEIGHT".format(x) for x in listOfParameters]


# Separator between tests
separator = "##########"

boolOptions = [True, False]

currPid = os.getpid()
currTime = datetime.datetime.now().strftime("%m-%d-%Y_%H-%M-%S")
outputFileName = "AutomatedTestInput_{}_{}.txt".format(currPid, currTime)
outputFilePath = os.path.join(execDir, outputFileName)


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser(description='Generated Automated Test Input.')
    parser.add_argument('--debug', required=False, action="store_true",
                        help="Enable to print Debug Messages.")
    parser.add_argument('--sentence', required=True, help="Sentence to test on.")
    args = parser.parse_args()

    # Set global debug flag.
    if args.debug:
        DEBUG = True

    testCounter = 1

    with open(outputFilePath, 'w') as outputFile:
        for sentenceBool in boolOptions:
            for lemmaBool in boolOptions:
                for stemBool in boolOptions:
                    for posTagBool in boolOptions:
                        for headWordBool in boolOptions:
                            for hypernymBool in boolOptions:
                                for hyponymBool in boolOptions:
                                    for meronymBool in boolOptions:
                                        for holonymBool in boolOptions:
                                            if sentenceBool is lemmaBool is stemBool is posTagBool is headWordBool is hypernymBool is hyponymBool is meronymBool is holonymBool is False:
                                                # If all false, then skip this option.
                                                continue

                                            # If here then at least one is true.
                                            outputFile.write(
                                                "#TESTNUMBER: {}\n".format(testCounter))
                                            outputFile.write(
                                                "SENTENCE: \"{}\"\n".format(args.sentence))
                                            outputFile.write("{}_FLAG: {}\n".format(
                                                "SENTENCE", sentenceBool))
                                            outputFile.write(
                                                "{}_WEIGHT: {}\n".format("SENTENCE", 1))
                                            outputFile.write(
                                                "{}_FLAG: {}\n".format("LEMMA", lemmaBool))
                                            outputFile.write("{}_WEIGHT: {}\n".format("LEMMA", 1))
                                            outputFile.write(
                                                "{}_FLAG: {}\n".format("STEM", stemBool))
                                            outputFile.write("{}_WEIGHT: {}\n".format("STEM", 1))
                                            outputFile.write(
                                                "{}_FLAG: {}\n".format("POSTAG", posTagBool))
                                            outputFile.write("{}_WEIGHT: {}\n".format("POSTAG", 1))
                                            outputFile.write("{}_FLAG: {}\n".format(
                                                "HEADWORD", headWordBool))
                                            outputFile.write(
                                                "{}_WEIGHT: {}\n".format("HEADWORD", 1))
                                            outputFile.write("{}_FLAG: {}\n".format(
                                                "HYPERNYM", hypernymBool))
                                            outputFile.write(
                                                "{}_WEIGHT: {}\n".format("HYPERNYM", 1))
                                            outputFile.write("{}_FLAG: {}\n".format(
                                                "HYPONYM", hyponymBool))
                                            outputFile.write("{}_WEIGHT: {}\n".format("HYPONYM", 1))
                                            outputFile.write("{}_FLAG: {}\n".format(
                                                "MERONYM", meronymBool))
                                            outputFile.write("{}_WEIGHT: {}\n".format("MERONYM", 1))
                                            outputFile.write("{}_FLAG: {}\n".format(
                                                "HOLONYM", holonymBool))
                                            outputFile.write("{}_WEIGHT: {}\n".format("HOLONYM", 1))
                                            outputFile.write("\n{}\n\n".format(separator))
                                            testCounter += 1
