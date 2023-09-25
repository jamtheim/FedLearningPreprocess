# Run MICE pre processing
# Overwrite with any manually corrected data points
# Christian had one with bad registrations 
# Activate virtual environment
source ./extractSt/bin/activate
# Run in serial order
python3 1.preProcessDataForTraining.py
python3 2.fuseDataAndAnonymise.py
python3 3.processAnonData.py
python3 4.stackData.py


