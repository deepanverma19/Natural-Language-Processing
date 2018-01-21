# Project
NLP Project

Running the program:
- You can always run the program with the "-h" flag to get help and see what arguments are available.

Example:
<pre>
python projectTask2.py -h
usage: projectTask2.py [-h] [--debug] [--trainData]
                       [--dataLocation DATALOCATION] [--userInput USERINPUT]

Task 2: Create a Shallow NLP Pipeline.

optional arguments:
  -h, --help            show this help message and exit
  --debug               Enable to print Debug Messages.
  --trainData           Train on the Corpus.
  --dataLocation DATALOCATION
                        Training Data location if not default.
  --userInput USERINPUT
                        Sentence to test on.
</pre>                        


Example of running the program with user input:<br />
<pre>python projectTask2.py --debug --userInput "This is a test sentence. How do you do? This is a third sentence."</pre>


Example of running the program to train based on the corpus:<br />
<pre>python projectTask2.py --debug --trainData</pre>


Example of running the program with user input AND also training based on the corpus:<br />
<pre>python projectTask2.py --debug --userInput "This is a test sentence. How do you do? This is a third sentence." --trainData</pre>

<br /><br />

<p>
  <b>REQUIREMENTS:</b><br />
  The training data must be located in a folder called "TrainingData" located in the same folder as projectTask2.py.
</p>

<br /><br />


### Part 3 Code
Run the same as part 2 code above.

To train based on the corpus:<br />
<pre>python projectTask3.py --trainData</pre>

To query user input:<br />
<pre>python projectTask3.py --userInput "who has support for Paris Accord"</pre>


### Automating the testing of Part 3 Code
You can specify the flag and the weight.  If the flag is NOT specified, that feature is not used in the query.
To do this testing you MUST include the "--testing" flag.

Here is an example of querying with all the features with weight 1 (NOTE: This is default behavior):<br />
<pre>python projectTask3.py --userInput "G-7 strengthens Paris Accord" --testing --sentenceFlag --sentenceWeight 1 --lemmaFlag --lemmaWeight 1 --stemFlag --stemWeight 1 --posTagFlag --posTagWeight 1 --headWordFlag --headWordWeight 1 --hypernymFlag --hypernymWeight 1 --hyponymFlag --hyponymWeight 1 --meronymFlag --meronymWeight 1 --holonymFlag --holonymWeight 1</pre>



### Setup Solr

1. Install Solr -v 7.1.0.
    * For mac: ``` $ brew install solr```
    * For Windows: Go to Mirror link [Solr](http://apache.mirrors.pair.com/lucene/solr/7.1.0)
      * Click on **solr-7.1.0.zip** link.

2. Start Solr
    * go to root folder of Solr.
      * For mac: ``` $ solr start -p 8983```
      * For Windows: ```bin\solr.cmd start```
    * Check status of Solr.
      * ```bin/solr status```, or
      * Go to ```http://localhost:8983/solr/```

3. Add Core
    * For mac: ``` $ solr create -c mycore```
    * For Windows: ```bin\solr.cmd create -c mycore```

4. ```$ pip3 install pysolr```

5. ```$ pip3 install codecs```

6. To start indexing, run the following command:</br>
<pre> $ python3 projectTask2.py --trainData </pre>

7. To query:</br>
<pre> $ python3 projectTask2.py --userInput "This is a test sentence. How do you do? This is a third sentence." </pre>





### Using runTestOnProject3.py
To run:<br />
<pre>python runTaskOnProject3.py --file FILENAME</pre>
FILENAME can be whatever input file you have that is in the format of AutomatedTestInput.txt<br /><br />


The script will output 3 files.  PID and TIMESTAMP are variables and may change between different runs:<br />
1) Project3Test_PID_TIMESTAMP.txt<br />
    a) This one will be used later in determining which variables have higher MRR.<br />
    b) NOT NEEDED RIGHT NOW.<br />
2) OutputSentencesToGradeTask3_PID_TIMESTAMP.txt<br />
    a) <b>This is the file you need to grade the sentences from.</b><br />
3) OutputRunAfterGradingSentences_PID_TIMESTAMP.txt<br />
    a) This one will be used later in determining which variables have higher MRR.<br />
    b) NOT NEEDED RIGHT NOW.<br />



### Installing Core NLP Server
<p>1) Install the following:
http://nlp.stanford.edu/software/stanford-corenlp-full-2017-06-09.zip
http://nlp.stanford.edu/software/stanford-english-corenlp-2017-06-09-models.jar

2) Go to the directory where you unzipped the file and place the JAR file in there

3) Run the following command in the directory: 
<pre>java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000</pre>

NOTE: You may have to change mx4g to be mx3g or mx2g or mx1g depending on your computer's resources.

</p>
