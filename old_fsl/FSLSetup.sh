# Run only if FSLDIR is not set
if [ -z ${FSLDIR} ]; then
    echo "Setting up FSL"
    FSLDIR=/home/mluser2/fsl
    . ${FSLDIR}/etc/fslconf/fsl.sh
    PATH=${FSLDIR}/bin:${PATH}
    export FSLDIR PATH
    # Print the FSLDIR and PATH variables to check they are set correctly
    echo $PATH

else
    echo "FSL already set up, not editing PATH"
    echo $PATH
fi


