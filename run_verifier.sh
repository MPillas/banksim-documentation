#!/bin/bash

echo "Remember to activate an environment! Here I used:"
echo "source /home/marion.pillas/project/example_documentation/env_py39/bin/activate"

pycbc_make_bank_verifier_workflow --config-files global_setup.ini --workflow-name bank_verificator --output-dir /home/marion.pillas/project/example\
_documentation/output_example_documentation_final/ --submit-now
