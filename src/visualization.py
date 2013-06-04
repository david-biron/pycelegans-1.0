'''This module defines the visualization routine'''

import os
import numpy
import scipy.ndimage

import libcelegans 

def viz(VIZDIR,NamePrefix,DiffImage,OrigImage,SideOnePath,SideTwoPath,Tail,Head,MidLine): 

    scipy.misc.imsave(os.path.join(VIZDIR,NamePrefix) + "nobg.jpg",DiffImage) 

    libcelegans.save_wormviz_image(VIZDIR,NamePrefix+"-viz.jpg" ,OrigImage,
    scipy.ndimage.morphology.binary_dilation(libcelegans.pointlist_to_array2(
     SideOnePath,numpy.zeros(numpy.shape(OrigImage))),iterations=1),
    scipy.ndimage.morphology.binary_dilation(libcelegans.pointlist_to_array2(
     SideTwoPath,numpy.zeros(numpy.shape(OrigImage))),iterations=1),
    scipy.ndimage.morphology.binary_dilation(Tail,iterations=5),
    scipy.ndimage.morphology.binary_dilation(Head,iterations=5),
    scipy.ndimage.morphology.binary_dilation(libcelegans.pointlist_to_array2(
     MidLine,numpy.zeros(numpy.shape(OrigImage))),iterations=1),
     )

