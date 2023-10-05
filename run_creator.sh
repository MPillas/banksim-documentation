#!/bin/sh

pycbc_create_injections --config-files broadinjs1_config.ini --output-file broad.hdf --ninjections 10 --seed 12  --verbose
pycbc_create_injections --config-files pointinj_1.12_1.07_config.ini --output-file point.hdf --ninjections 10 --seed 12  --verbose
