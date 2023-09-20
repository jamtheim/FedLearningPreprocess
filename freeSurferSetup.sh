# Download free surfer and put in home directory
# https://surfer.nmr.mgh.harvard.edu/fswiki/DownloadAndInstall
# Tested with Latest Version 7 Release is 7.4.1 (June 2023)

# Run only if FREESURFER_HOME is not set
if [ -z ${FREESURFER_HOME} ]; then
    echo "Setting up FreeSurfer..."
    export FREESURFER_HOME=$HOME/freesurfer
    source $FREESURFER_HOME/SetUpFreeSurfer.sh
    echo "FreeSurfer is set up!"
else
    echo "FreeSurfer path already set up..."
fi