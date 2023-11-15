############################################################################
``pycbc_make_bank_verifier_workflow``: A bank verificator workflow generator
############################################################################

===============
Introduction
===============

The executable ``pycbc_make_bank_verifier_workflow`` is a workflow generator that verifies the ability of a template bank to recover sets of injections. It can be setup to run on one or more injection sets simultaneously. For each injection set, the workflow:

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

The workflow generator also needs configuration files that indicate the parameter space covered by the injections. These are separate from the workflow configuration file.
The bank verificator workflow requires at least one set of broad injections (scattered over the parameter space) and one of point injections (at ~fix masses).
Multiple sets of broad/point injections can be given by creating more dedicated configuration files and thus adding sections to the workflow configuration file.
To create a large set of point injections, we can write the configuration file using a Python helper script to generate as many new sections as there are point injections.

A path to a Python script called ``filter_func.py`` should also be provided. 

During the previous observing runs, the waveforms from the template bank PyCBC were subject to a cut based on their duration: the bank does not include templates shorter than 0.15 seconds. This threshold has historically been placed because approximants used in previous runs (2015-2016) did not work with such duration. Nowadays, this cut is still applied to prevent the search from being contaminated by short-duration glitches that match the time-frequency shape of the GW signal, making them challenging to distinguish (see Dal Canton & Harry, 2017).

One way to get this filter function is to download and copy the script in the same repository as the configuration files. 

This script creates versions of the final results plots in which short-duration injections are ignored. The threshold on the duration, the approximant used to compute it and the ASD file should be changed according to your needs by modifying your copy of the script.

To illustrate how to setup and use a workflow, below we provide an example of how to setup the workflow to analyze BBH, NSBH and BNS injections.
This workflow will produce a results page that looks like the example
`Bank verifier BBH, NSBH and BNS injections <https://ldas-jobs.ligo.caltech.edu/~marion.pillas/example_doc_banksim/bank_output_example_documentation_BBH_BNS_NSBH_final/>`_. 

--------------------------------------------
Get the injection configuration files
--------------------------------------------
**Broad injections:**

.. literalinclude:: broadinjs1_config.ini
   :language: ini

:download:`Download <broadinjs1_config.ini>`

**Point injections:**

.. literalinclude:: pointinj_1.12_1.07_config.ini
   :language: ini

:download:`Download <pointinj_1.12_1.07_config.ini>`

--------------------------------------------
Setup the workflow configuration file
--------------------------------------------

.. literalinclude:: global_setup.ini
   :language: ini

:download:`Download <global_setup.ini>`

**Notes:**

* In the ``[pegasus_profile]`` section an accounting group should be specified *if* running on LDG resources. For non-LVK people this is not needed.

* If the jobs take too long to run, you can increase the ``splittable-num-banks`` parameter both for ``[workflow-splittable-*injbanksplit]`` and ``[workflow-splittable-*injs]``.

* Change the ``seed`` everytime you create a different workflow.
This sets the seed that is passed to ``pycbc_hdf5_splitbank`` (you set it here
because it will be incremented for every ``splitbank`` job that will be
run in the workflow).

--------------------------------------------
Get the filter function
--------------------------------------------
.. literalinclude:: filter_func.py
   :language: python

:download:`Download <filter_func.py>`

--------------------------------------------
Generate and submit the workflow
--------------------------------------------

Assuming that you have downloaded all of the configuration files to the
same directory, you can generate the workflow by running the following script:

.. literalinclude:: run_verifier.sh
   :language: bash

:download:`Download <run_verifier.sh>`

Note that you need to set the ``output-dir`` before running. This tells the
workflow where to save the results page when done. You can also change
``workflow-name`` if you like.

Finally, the argument ``submit-now`` automatically plans and submits the workflow.

Once it is running, you can monitor the status of the workflow by running
``./status`` from within the ``output-dir`` directory. If your
workflow fails for any reason, you can see what caused the failure by running
``./debug``. If you need to stop the workflow at any point, run ``./stop``.
To resume a workflow, run ``./start``. 

------------
Results page
------------
When the workflow has completed successfully it will write out the results
page to the directory you specified as ``output-path`` in the ``[results_page]`` section of ``global_setup.ini``.
You can see what the result page will look like the example `Bank verifier BBH injections <https://ldas-jobs.ligo-wa.caltech.edu/~marion.pillas/template_bank/O3PSD/BBH/bank_output_BBH/>`_. 
