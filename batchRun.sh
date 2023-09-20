
# Activate virtual environment
source ./extractSt/bin/activate
# Run in serial order
python3 1.preProcessDataForTraining.py
sleep 10 
python3 2.fuseDataAndAnonymise.py
sleep 10 
python3 3.processAnonData.py
sleep 10 
python3 4.stackData.py

