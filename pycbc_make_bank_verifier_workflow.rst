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
#. Concatenates output files from ``pycbc_banksim`` split over bank files using ``pycbc_banksim_combine_banks``.
#. Concatenates output files from pycbc_banksim_combine_banks with a set of injection files running ``pycbc_banksim_match_combine``.
#. Makes a summary result table for a set of point injection runs with ``pycbc_banksim_table_point_injs``.
#. Creates diagnosis plots and figures of merit
