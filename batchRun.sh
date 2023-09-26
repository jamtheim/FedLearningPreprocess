# 0. Run MICE pre processing
# Overwrite with any manually corrected data points
# Christian had one with bad automatic registrations 

# Activate virtual environment
source ./extractSt/bin/activate

# Run in serial order
python3 1.preProcessDataForTraining.py
python3 2.fuseDataAndAnonymise.py
python3 3.processAnonData.py
python3 4.stackData.py
python3 5.aggregateFinalDataScaleout.py # Put all data from all cohorts in the same data folder for Scalout
python3 6.aggregateFinalDataIfusion.py # Put all data from all cohorts in the same data folder for Ifusion. Creates JSON file. 



