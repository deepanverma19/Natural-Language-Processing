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
import sys
import argparse
import subprocess
import datetime
import platform

# For Testing Purposes.
### DO NOT MAKE CHANGES TO TESTING VARIABLE HERE ###
### ONLY MAKE CHANGES FROM COMMAND-LINE OPTIONS ###
DEBUG = False  # True/False.

# Get directory of executable files are located in relative to python file.
execDir = os.path.dirname(os.path.realpath(__file__))

# Generate filename based on PID of process and datetime.
# Include PID in case we want to run multiple instances concurrently, then each PID has a separate output file.
currPid = os.getpid()
currTime = datetime.datetime.now().strftime("%m-%d-%Y_%H-%M-%S")
outputFileName = "Project3Test_{}_{}.txt".format(currPid, currTime)
outputFilePath = os.path.join(execDir, outputFileName)
outputRunAfterGradingSentencesName = "OutputRunAfterGradingSentences_{}_{}.txt".format(
    currPid, currTime)
outputRunAfterGradingSentencesPath = os.path.join(execDir, outputRunAfterGradingSentencesName)
outputSentencesToGradeName = "OutputSentencesToGradeTask3_{}_{}.txt".format(currPid, currTime)
outputSentencesToGradeFilePath = os.path.join(execDir, outputSentencesToGradeName)

# Dictionary to hold each unique sentence found based on DocSentenceID
UniqueSentences = {}


def printDebugMsg(text):
    """Used for printing debug messages."""
    if DEBUG:
        print(text)


# Separator between tests
separator = "##########"

if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser(description='Run Automated Tests on Project 3')
    parser.add_argument('--debug', required=False, action="store_true",
                        help="Enable to print Debug Messages.")
    parser.add_argument('--file', required=True, help="AutomatedTestInput file")
    args = parser.parse_args()

    # Set global debug flag.
    if args.debug:
        DEBUG = True

    if not os.path.isfile(args.file):
        print("ERROR: {} does not exist".format(args.file))

    with open(os.path.join(execDir, args.file), 'r') as inputFile:
        # initialize to None to make sure nothing was missed.
        testNumber = None
        querySentence = None
        sentenceFlag = sentenceWeight = None
        lemmaFlag = lemmaWeight = None
        stemFlag = stemWeight = None
        posTagFlag = posTagWeight = None
        headWordFlag = headWordWeight = None
        hypernymFlag = hypernymWeight = None
        hyponymFlag = hyponymWeight = None
        meronymFlag = meronymWeight = None
        holonymFlag = holonymWeight = None
        listOfVariableValues = []

        for line in inputFile:
            line = line.strip("\r\n")
            printDebugMsg(line)

            # Maintain list of variables for output
            if (separator not in line) and (len(line) != 0):
                listOfVariableValues.append(line)

            if separator in line:
                # Finished collecting information for test.  Now run the test.

                # Check that all the information has been collected
                if (testNumber is None) or (querySentence is None) or \
                    (sentenceFlag is None) or (sentenceWeight is None) or \
                    (lemmaFlag is None) or (lemmaWeight is None) or \
                    (stemFlag is None) or (stemWeight is None) or \
                    (posTagFlag is None) or (posTagWeight is None) or \
                    (headWordFlag is None) or (headWordWeight is None) or \
                    (hypernymFlag is None) or (hypernymWeight is None) or \
                    (hyponymFlag is None) or (hyponymWeight is None) or \
                    (meronymFlag is None) or (meronymWeight is None) or \
                        (holonymFlag is None) or (holonymWeight is None):
                    print("ERROR: Missing data. Please verify the format is correct and try again. Exiting...")
                    sys.exit(1)

                # If here then we have all the data.
                # Initialize list here.  querySentence has to be put together intact into the list.
                # All other parameters can be put in and split using space later.

                if platform.system() == 'Windows':
                    # Windows syntax
                    commandToRunList = ["python", "projectTask3.py",
                                        "--userInput", querySentence, "--testing"]
                else:
                    # Mac/Linux syntax
                    commandToRunList = ["python3", "projectTask3.py",
                                        "--userInput", querySentence, "--testing"]

                remainingCommandToRun = ""
                if sentenceFlag:
                    remainingCommandToRun += "--sentenceFlag --sentenceWeight {} ".format(
                        sentenceWeight)
                if lemmaFlag:
                    remainingCommandToRun += "--lemmaFlag --lemmaWeight {} ".format(lemmaWeight)
                if stemFlag:
                    remainingCommandToRun += "--stemFlag --stemWeight {} ".format(stemWeight)
                if posTagFlag:
                    remainingCommandToRun += "--posTagFlag --posTagWeight {} ".format(posTagWeight)
                if headWordFlag:
                    remainingCommandToRun += "--headWordFlag --headWordWeight {} ".format(
                        headWordWeight)
                if hypernymFlag:
                    remainingCommandToRun += "--hypernymFlag --hypernymWeight {} ".format(
                        hypernymWeight)
                if hyponymFlag:
                    remainingCommandToRun += "--hyponymFlag --hyponymWeight {} ".format(
                        hyponymWeight)
                if meronymFlag:
                    remainingCommandToRun += "--meronymFlag --meronymWeight {} ".format(
                        meronymWeight)
                if holonymFlag:
                    remainingCommandToRun += "--holonymFlag --holonymWeight {} ".format(
                        holonymWeight)

                printDebugMsg(remainingCommandToRun)

                # commandToRunList = ['python', 'projectTask3.py', '--userInput', '"G-7 strengthens Paris Accord"', '--testing', '--sentenceFlag', '--sentenceWeight', '1', '--lemmaFlag', '--lemmaWeight', '1', '--stemFlag', '--stemWeight', '1', '--posTagFlag',
                #                     '--posTagWeight', '1', '--headWordFlag', '--headWordWeight', '1', '--hypernymFlag', '--hypernymWeight', '1', '--hyponymFlag', '--hyponymWeight', '1', '--meronymFlag', '--meronymWeight', '1', '--holonymFlag', '--holonymWeight', '1']

                # Subprocess requires list of commands, where each value is an item in the list.
                remainingCommandToRunList = remainingCommandToRun.split(" ")

                # May have extra space at the end, so remove it if it does.
                if remainingCommandToRunList[-1:] == [""]:
                    lengthOfList = len(remainingCommandToRunList) - 1
                    remainingCommandToRunList = remainingCommandToRunList[:lengthOfList]

                # Extend initial list with parameters from list we just populated.
                commandToRunList.extend(remainingCommandToRunList)
                printDebugMsg("commandToRunList is: {}".format(commandToRunList))
                scriptOutput = bytes.decode(subprocess.check_output(commandToRunList))
                printDebugMsg("scriptOutput is {}".format(scriptOutput))

                # Parse scriptOutput
                for line in scriptOutput.split("\n"):
                    # Skip blank lines in output.
                    if len(line) < 3:
                        continue

                    # QUERY_FLAG in projectTask3 will output extra info. Ignore it.
                    try:
                        lineNumber, docID, sentence = line.split("\t")
                    except ValueError:
                        continue

                    sentence = sentence.strip("\r\n")
                    UniqueSentences[docID] = sentence

                    with open(outputRunAfterGradingSentencesPath, 'a') as outputAfterGradingFile:
                        outputAfterGradingFile.write(
                            "{}\t{}\t{}\t{}\n".format(testNumber, lineNumber, docID, sentence))

                # Run original file output
                with open(outputFilePath, 'a') as outputFile:
                    # Write input parameters for test.
                    outputFile.write("{}\n\n".format("\n".join(listOfVariableValues)))
                    # Write buffer
                    outputFile.write("=====\n\n")
                    # Write output of test.
                    outputFile.write("{}\n\n".format(scriptOutput))
                    # Write separator twice
                    outputFile.write("{}{}\n\n".format(separator, separator))

                # Reset variables to None to make sure nothing was missed.
                testNumber = None
                querySentence = None
                sentenceFlag = sentenceWeight = None
                lemmaFlag = lemmaWeight = None
                stemFlag = stemWeight = None
                posTagFlag = posTagWeight = None
                headWordFlag = headWordWeight = None
                hypernymFlag = hypernymWeight = None
                hyponymFlag = hyponymWeight = None
                meronymFlag = meronymWeight = None
                holonymFlag = holonymWeight = None
                listOfVariableValues = []

            elif "#TESTNUMBER:" in line:
                # Used for output.
                testNumber = line
            elif "SENTENCE:" in line:
                querySentence = line.split(": ")[1]
            elif "SENTENCE_FLAG" in line:
                value = line.split(": ")[1]
                if value == "True":
                    sentenceFlag = True
                else:
                    sentenceFlag = False
            elif "SENTENCE_WEIGHT" in line:
                value = line.split(": ")[1]
                sentenceWeight = int(value)
            elif "LEMMA_FLAG" in line:
                value = line.split(": ")[1]
                if value == "True":
                    lemmaFlag = True
                else:
                    lemmaFlag = False
            elif "LEMMA_WEIGHT" in line:
                value = line.split(": ")[1]
                lemmaWeight = int(value)
            elif "STEM_FLAG" in line:
                value = line.split(": ")[1]
                if value == "True":
                    stemFlag = True
                else:
                    stemFlag = False
            elif "STEM_WEIGHT" in line:
                value = line.split(": ")[1]
                stemWeight = int(value)
            elif "POSTAG_FLAG" in line:
                value = line.split(": ")[1]
                if value == "True":
                    posTagFlag = True
                else:
                    posTagFlag = False
            elif "POSTAG_WEIGHT" in line:
                value = line.split(": ")[1]
                posTagWeight = int(value)
            elif "HEADWORD_FLAG" in line:
                value = line.split(": ")[1]
                if value == "True":
                    headWordFlag = True
                else:
                    headWordFlag = False
            elif "HEADWORD_WEIGHT" in line:
                value = line.split(": ")[1]
                headWordWeight = int(value)
            elif "HYPERNYM_FLAG" in line:
                value = line.split(": ")[1]
                if value == "True":
                    hypernymFlag = True
                else:
                    hypernymFlag = False
            elif "HYPERNYM_WEIGHT" in line:
                value = line.split(": ")[1]
                hypernymWeight = int(value)
            elif "HYPONYM_FLAG" in line:
                value = line.split(": ")[1]
                if value == "True":
                    hyponymFlag = True
                else:
                    hyponymFlag = False
            elif "HYPONYM_WEIGHT" in line:
                value = line.split(": ")[1]
                hyponymWeight = int(value)
            elif "MERONYM_FLAG" in line:
                value = line.split(": ")[1]
                if value == "True":
                    meronymFlag = True
                else:
                    meronymFlag = False
            elif "MERONYM_WEIGHT" in line:
                value = line.split(": ")[1]
                meronymWeight = int(value)
            elif "HOLONYM_FLAG" in line:
                value = line.split(": ")[1]
                if value == "True":
                    holonymFlag = True
                else:
                    holonymFlag = False
            elif "HOLONYM_WEIGHT" in line:
                value = line.split(": ")[1]
                holonymWeight = int(value)
            elif len(line) == 0:
                # Blank line
                continue

    # Run variables to grade output
    with open(outputSentencesToGradeFilePath, 'a') as outputGradeFile:
        for key, val in UniqueSentences.items():
            outputGradeFile.write("{}\t{}\n".format(key, val))
