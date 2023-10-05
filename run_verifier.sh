#!/bin/bash

echo "Remember to activate a conda environment! Some common choices are:"
echo "conda deactivate; conda activate /home/francesco.pannarale/.conda/envs/pygrb_devel"
echo "conda deactivate; conda activate /home/lorenzo.piccari/.conda/envs/pycbc_tesi"
echo

pycbc_make_bank_verifier_workflow --config-files global_setup.ini --workflow-name bank_verificator --output-dir /PATH/TO/OUTPUT/DIRECTORY --submit-now
