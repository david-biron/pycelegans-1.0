pycelegans
==========

Parallel image processing code that identifies C. elegans in images


Contact
========
David Biron
Assistant Professor
Department of Physics
dbiron@uchicago.edu

Nicholas Labello
Scientific Computing Consultant
UChicago Research Computing Center
labello@uchicago.edu


Note
=====

This code is an ongoing research project.  You are encouraged to contact us 
before installing it.

The requirements to run the code are a Python 2.7 environment and the addons
NumPy, SciPy, PyMorph, and Scikits-Image. MPI4Py is required for multi-node
parallelism.


Timing
======

Run on the University of Chicago Research Computing Center
Midway cluster (rcc.uchicago.edu). The CPU model is Intel
Xeon CPU E5-2670 0 @ 2.60GHz.

 Time to process 1000 images

  Cores | Visualization-Off
    8   | 144.5
   16   |  85.5
   32   |  46.0
   64   |  25.7
