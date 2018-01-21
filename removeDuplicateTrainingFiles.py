# CS 6320 - Natural Language Processing
# Group Project
#
# Remove duplicates from corpus
#
# Authors:
#       Stephen Blystone (smb032100@utdallas.edu)
#       Amit Gupta (axg162930@utdallas.edu)
#       Deepan Verma (dxv160430@utdallas.edu)
#
# Teamname:
#       GASBDV (General Anakin Skywalker Becomes Darth Vader)

import os


# For Testing Purposes.
### DO NOT MAKE CHANGES TO TESTING VARIABLE HERE ###
### ONLY MAKE CHANGES FROM COMMAND-LINE OPTIONS ###
DEBUG = False  # True/False.

# Get directory of executable files are located in relative to python file.
execDir = os.path.dirname(os.path.realpath(__file__))

# Variable to hold training data location.  Can change via command-line parameter.
trainingDataDir = os.path.join(execDir, "TrainingData")


def printDebugMsg(text):
    """Used for printing debug messages."""
    if DEBUG:
        print(text)

# fileTestList = ["15442", "15449", "15460"]


keepAlgNFactorial = set()

filesToRemove = set()
filesToKeep = set()

for currFile in os.listdir(trainingDataDir):
    for compFile in os.listdir(trainingDataDir):
        # print("currFile is {}".format(currFile))
        # print("compFile is {}".format(compFile))
        # If same file, move on.
        if currFile == compFile:
            # print("same")
            continue

        # check if compared the files before
        if ("{}_{}".format(currFile, compFile) in keepAlgNFactorial) or ("{}_{}".format(compFile, currFile) in keepAlgNFactorial):
            # print("seen before")
            continue

        # If here then haven't seen this combination before.

        # Add to keepAlgNFactorial so we don't repeat ourselves.
        keepAlgNFactorial.add("{}_{}".format(currFile, compFile))

        with open(os.path.join(trainingDataDir, currFile), "r") as file1:
            file1Data = file1.read()
            file1Length = len(file1Data)

        with open(os.path.join(trainingDataDir, currFile), "r") as file1:
            file1Line = file1.readline()

        with open(os.path.join(trainingDataDir, compFile), "r") as file2:
            file2Data = file2.read()
            file2Length = len(file2Data)

        with open(os.path.join(trainingDataDir, compFile), "r") as file2:
            file2Line = file2.readline()

        # print("file1Line is: {}".format(file1Line))
        # print("file2Line is: {}".format(file2Line))
        if ((file1Line == file2Line) and (file2Length >= file1Length)):
            # print("{} is contained in {}".format(currFile, compFile))
            print("{} vs. {}: {} == {} and {} >= {}".format(
                currFile, compFile, file1Line, file2Line, file2Length, file1Length))
            filesToRemove.add(currFile)
            filesToKeep.add(compFile)
        elif ((file2Line == file1Line) and (file1Length >= file2Length)):
            # print("{} is contained in {}".format(compFile, currFile))
            print("{} vs. {}: {} == {} and {} >= {}".format(
                compFile, currFile, file2Line, file1Line, file1Length, file2Length))
            filesToRemove.add(compFile)
            filesToKeep.add(currFile)
        else:
            # Good, nothing in common.
            pass

# Go through and remove any from filesToKeep that are also in filesToRemove
for currFile in filesToRemove:
    if currFile in filesToKeep:
        filesToKeep.remove(currFile)
    print("Remove {}".format(currFile))
    os.remove(os.path.join(trainingDataDir, currFile))

for currFile in filesToKeep:
    print("Keep {}".format(currFile))
