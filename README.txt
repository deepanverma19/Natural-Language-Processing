Teamname:
      GASBDV (General Anakin Skywalker Becomes Darth Vader)
Authors:
      Stephen Blystone (smb032100@utdallas.edu)
      Amit Gupta (axg162930@utdallas.edu)
      Deepan Verma (dxv160430@utdallas.edu)

	  
Software Requirements:
	Download, Installation, and Running Instructions specified in the FinalReport.docx
	
	
Files/Folders:
	1) TrainingData
		-Contains training data used for our project.
		-This data has duplicates articles removed.
	
	2) checkCorpusForDuplicates.py
		-File for Task 1
		-Counts number of words, sentences, and documents. Also checks for duplicate files.
		-To Run:
			python checkCorpusForDuplicates.py
		
	3) removeDuplicateTrainingFiles.py
		-File for Task 1
		-Removes duplicates from the Training Data
		-To Run:
			python removeDuplicateTrainingFiles.py
		
	4) projectTask2.py
		-File for Task 2
		-To Index:
			python projectTask2.py --trainData
		-To Query:
			python projectTask2.py --userInput "Australia is more competitive than the U.S."
			
	5) projectTask3.py
		-File for Task 3
		-To Index:
			python projectTask3.py --trainData
		-To Query:
			python projectTask3.py --userInput "Australia is more competitive than the U.S."
	
	6) generateAutomatedTestInput.py
		-File for Task 4
		-Generates all combinations of features (all with weight 1).
		-Outputs AutomatedTestFile
		-To Run:
			python generateAutomatedTestInput.py --sentence "Australia is more competitive than the U.S."
	
	7) AutomatedTestInput_26284_12-06-2017_13-09-08.txt
		-File for Task 4
		-Sample output from generateAutomatedTestInput.py
		
	8) AutomatedTestWeights.txt
		-File for Task 4
		-Test file built to test each query with the features and weights we selected.
	
	9) runTestOnProject3.py
		-File for Task 4
		-Runs the appropriate command-line parameters when calling projectTask3.py for the features and weights in the AutomatedTestFile.
		-To Run:
			python runTestOnProject3.py --file AutomatedTestInput_26284_12-06-2017_13-09-08.txt
	
	10) MRR_Analysis.xlsb
		-File for Task 4
		-Using the output files from runTestOnProject3.py, we can calculate the MRR using Excel formulas.
		
	11) FinalReport.docx
		-The final report.
		
	12) ProjectGroupInfo-GeneralAnakinSkywalkerBecomesDarthVader.pdf
		Project Group Info
		
	
		
Part 2 Queries:
	python projectTask2.py --userInput "G-7 support for the Paris Agreement"
	python projectTask2.py --userInput "Selling cows to Indonesia"
	python projectTask2.py --userInput "Increase loans in Virginia"
	python projectTask2.py --userInput "Thailand tin export company"
	python projectTask2.py --userInput "Aramco field oil reserves increase"
	python projectTask2.py --userInput "Australia is more competitive than the U.S."
	python projectTask2.py --userInput "China buying grain"
	python projectTask2.py --userInput "Shareholders vote on buyout"
	python projectTask2.py --userInput "Indonesia importing oil"
	python projectTask2.py --userInput "Australia's economy performs well"
	
	
Part 3 Queries:
	python projectTask3.py --userInput "G-7 support for the Paris Agreement"
	python projectTask3.py --userInput "Selling cows to Indonesia"
	python projectTask3.py --userInput "Increase loans in Virginia"
	python projectTask3.py --userInput "Thailand tin export company"
	python projectTask3.py --userInput "Aramco field oil reserves increase"
	python projectTask3.py --userInput "Australia is more competitive than the U.S."
	python projectTask3.py --userInput "China buying grain"
	python projectTask3.py --userInput "Shareholders vote on buyout"
	python projectTask3.py --userInput "Indonesia importing oil"
	python projectTask3.py --userInput "Australia's economy performs well"
	
	
Part 4 Queries (using features and weights we selected):
	python projectTask3.py --userInput "G-7 support for the Paris Agreement" --testing --sentenceFlag --sentenceWeight 1 --lemmaFlag --lemmaWeight 100 --stemFlag --stemWeight 50 --posTagFlag --posTagWeight 50 --holonymFlag --holonymWeight 50
	python projectTask3.py --userInput "Selling cows to Indonesia" --testing --sentenceFlag --sentenceWeight 1 --lemmaFlag --lemmaWeight 100 --stemFlag --stemWeight 50 --posTagFlag --posTagWeight 50 --holonymFlag --holonymWeight 50
	python projectTask3.py --userInput "Increase loans in Virginia" --testing --sentenceFlag --sentenceWeight 1 --lemmaFlag --lemmaWeight 100 --stemFlag --stemWeight 50 --posTagFlag --posTagWeight 50 --holonymFlag --holonymWeight 50
	python projectTask3.py --userInput "Thailand tin export company" --testing --sentenceFlag --sentenceWeight 1 --lemmaFlag --lemmaWeight 100 --stemFlag --stemWeight 50 --posTagFlag --posTagWeight 50 --holonymFlag --holonymWeight 50
	python projectTask3.py --userInput "Aramco field oil reserves increase" --testing --sentenceFlag --sentenceWeight 1 --lemmaFlag --lemmaWeight 100 --stemFlag --stemWeight 50 --posTagFlag --posTagWeight 50 --holonymFlag --holonymWeight 50
	python projectTask3.py --userInput "Australia is more competitive than the U.S." --testing --sentenceFlag --sentenceWeight 1 --lemmaFlag --lemmaWeight 100 --stemFlag --stemWeight 50 --posTagFlag --posTagWeight 50 --holonymFlag --holonymWeight 50
	python projectTask3.py --userInput "China buying grain" --testing --sentenceFlag --sentenceWeight 1 --lemmaFlag --lemmaWeight 100 --stemFlag --stemWeight 50 --posTagFlag --posTagWeight 50 --holonymFlag --holonymWeight 50
	python projectTask3.py --userInput "Shareholders vote on buyout" --testing --sentenceFlag --sentenceWeight 1 --lemmaFlag --lemmaWeight 100 --stemFlag --stemWeight 50 --posTagFlag --posTagWeight 50 --holonymFlag --holonymWeight 50
	python projectTask3.py --userInput "Indonesia importing oil" --testing --sentenceFlag --sentenceWeight 1 --lemmaFlag --lemmaWeight 100 --stemFlag --stemWeight 50 --posTagFlag --posTagWeight 50 --holonymFlag --holonymWeight 50
	python projectTask3.py --userInput "Australia's economy performs well" --testing --sentenceFlag --sentenceWeight 1 --lemmaFlag --lemmaWeight 100 --stemFlag --stemWeight 50 --posTagFlag --posTagWeight 50 --holonymFlag --holonymWeight 50
