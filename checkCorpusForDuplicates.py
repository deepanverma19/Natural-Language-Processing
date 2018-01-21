# CS 6320 - Natural Language Processing
# Group Project
#
# Check corpus for duplicates.
#
# Authors:
#       Stephen Blystone (smb032100@utdallas.edu)
#       Amit Gupta (axg162930@utdallas.edu)
#       Deepan Verma (dxv160430@utdallas.edu)
#
# Teamname:
#       GASBDV (General Anakin Skywalker Becomes Darth Vader)
import os
import codecs
import nltk
from nltk.tokenize import sent_tokenize


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


def segmentIntoSentences(article):
    """Segment article into sentences using NLTK.

    Input:
        -article: article to segment.
    Output:
        -list of sentences.
    """
    outputSentences = sent_tokenize(article)

    printDebugMsg("article is {}".format(article))
    printDebugMsg("outputSentences are {}".format(outputSentences))

    return outputSentences


def tokenizeIntoWords(sentence):
    """Tokenize sentence into words using NLTK.

    Input:
        -sentence: sentence to tokenize.
    Output:
        -list of words.
    """
    # sentence = re.sub(r'\W', ' ',sentence)
    outputWords = nltk.word_tokenize(sentence)

    printDebugMsg("sentence is {}".format(sentence))
    printDebugMsg("words are {}".format(outputWords))

    return outputWords


uniqueSentences = set()
duplicateFiles = {}
totalNumberSentences = 0

if os.path.exists(os.path.join(execDir, "CorpusDuplicateCheck.xls")):
    os.truncate(os.path.join(execDir, "CorpusDuplicateCheck.xls"), 0)

for trainFile in os.listdir(trainingDataDir):
    # Reads the file text as utf-8 coded text and ignores that can't be read.
    with codecs.open(os.path.join(trainingDataDir, trainFile), "r", encoding='utf-8', errors='ignore') as currFile:
        currFileData = currFile.read()

    # Use file data as key in dictionary.
    # If already exists, append filename to list.
    if currFileData in duplicateFiles:
        duplicateFiles[currFileData].append(trainFile)
    else:
        # First time seeing data. create new list.
        duplicateFiles[currFileData] = [trainFile]

    for sentence in segmentIntoSentences(currFileData):
        totalNumberSentences += 1
        uniqueSentences.add(sentence)

wordCounter = 0

for sentence in uniqueSentences:
    for word in tokenizeIntoWords(sentence):
        wordCounter += 1


print("Number of Unique Files: {}".format(len(duplicateFiles)))
print("Number of Unique Sentences: {}".format(len(uniqueSentences)))
print("Total Number of Sentences: {}".format(totalNumberSentences))
print("Number of Words in Unique Sentences: {}".format(wordCounter))

# After finished, print it out.
with open(os.path.join(execDir, "CorpusDuplicateCheck.xls"), "a") as outputFile:
    for data, listVal in duplicateFiles.items():
        if len(listVal) != 1:
            outputFile.write("{}\n".format("\t".join(listVal)))
