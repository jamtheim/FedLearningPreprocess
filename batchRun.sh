
# Activate virtual environment
source ./extractSt/bin/activate

python3 1.preProcessDataForTraining.py
#sleep 5
python3 2.fuseDataAndAnonymise.py
#sleep 5
python3 3.processAnonData.py
#sleep 5
python3 4.stackData.py

