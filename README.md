# README

Below, you may find instructions regarding how to set this project up.

1. Clone the repository.
2. Make sure you have pip installed.
3. Setup the project in PyCharm and configure the interpreter as Python 3.
4. Mark the src directory as sources root. You can do this by right clicking on the src directory in PyCharm.
4. Install all required libraries by typing 'pip install -r requirements.txt'.

Below, you may find instructions regarding how to find the sentiment associated with a university.

1. You can run the program by right clicking test_university.py and clicking 'run...'
2. Or you can cd into the src directory and type 'python3 test_university.py' in the PyCharm terminal and results will be printed in the console.
3. The default university is set to Texas A&M. If you wish to change this, type out the university csv file name on line 15 in test_university.py.

Please note that this is just a demonstration of the core algorithm using 400,000 data points to train the model. In the real working system, we plan on using 1.6 million tweets (800k positive / negative) to train the model.
