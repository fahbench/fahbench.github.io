#!/bin/bash

rm -r ../_api html latex xml

doxygen ../fahbench/doc/Doxyfile
python doxy-to-md.py
