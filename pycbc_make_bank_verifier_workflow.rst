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
#. Creates diagnosis plots and figures of merit using ``pycbc_banksim_plot_eff_fitting_factor`` and ``pycbc_banksim_plot_fitting_factors``.
#. Generates a results html page that gathers all of the results with ``pycbc_make_html_page``.

The workflow generator requires a configuration file that tells it how to split the bank and the injections, and any other settings to use for the various executables that are run.

The workflow generator also needs configuration files that indicate the parameter space covered by the injections. These are separate from the workflow configuration file
The bank verificator workflow requires at least one set of broad injections (scattered over the parameter space) and one of point injections (at ~fix masses).
Multiple sets of broad/point injections can be given by creating more dedicated configuration files and thus adding sections to the workflow configuration file.

A path to a Python script called ``filter_func.py`` should also be provided. One way to proceed is to download and copy the script in the same repository as the configuration files.

To illustrate how to setup and use a workflow, below we provide an example
of how to setup the workflow to analyze

