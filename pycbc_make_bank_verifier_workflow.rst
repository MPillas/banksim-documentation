############################################################################
``pycbc_make_bank_verifier_workflow``: A bank verificator workflow generator
############################################################################

===============
Introduction
===============

The executable ``pycbc_make_bank_verifier_workflow`` is a workflow generator that verifies the ability of a template bank to recover sets of injections. It can be setup to run on one or more
injection sets simultaneously. For each event, the workflow:

#. Splits the bank file running ``pycbc_hdf5_splitbank``. We suggest using a template bank in an HDF format, but if the bank is in an XML format, the script to use is ``pycbc_splitbank`` (see below the configuration files). 
#. Runs ``pycbc_create_injections`` to generate injections covering the parameter space given in the configuration file. Several sets of injections can be specified in the configuration files.
#. Splits the injections with ``pycbc_split_inspinj``.
#. Runs ``pycbc_banksim`` to calculate the fitting factors of the simulated signals with the template bank.
