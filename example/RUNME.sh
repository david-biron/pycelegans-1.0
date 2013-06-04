
###############################################################################
# (1) Generate a composite background image

python ../src/background.py --imgdir ./input --windowsize 10000

mv background_max_window_0000000_0003599.jpg background.jpg

# background.jpg will now exist in the working 
# directory

###############################################################################
# (2) Run the processing code

python ../src/processcelegans.py --np 16 --imgdir ./input --doviz yes 
python ../src/collectoutput.py ./scratch

# The processcelegans command above uses Python's included multiprocessing 
# library to distribute work to processors on one workstation.  If your machine
# has MPI you can try to run the code with a command like
#
#    mpirun -np 32 ../src/processcelegans.py --imgdir ./input --doviz yes
#
# MPI is only used to distribute the processes over a cluster.  The image
# processing scripts are not themselves parallel.

###############################################################################
# (3) Output will be found in the 'properties' and 'vizdir' directories.

###############################################################################
# (4) Clean up

rm ./scratch/*.pickle
rmdir ./scratch
