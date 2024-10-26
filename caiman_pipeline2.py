# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 14:51:27 2019

@author: Wei
"""

#!/usr/bin/env python

"""
Complete pipeline for motion correction, source extraction, and deconvolution
of one photon microendoscopic calcium imaging data using the CaImAn package.
The demo demonstrates how to use the params, MotionCorrect and cnmf objects
for processing 1p microendoscopic data. The analysis pipeline is similar as in
the case of 2p data processing with core difference being the usage of the
CNMF-E algorithm for source extraction (as opposed to plain CNMF). Check
the companion paper for more details.

You can also run a large part of the pipeline with a single method
(cnmf.fit_file) See inside for details.

Demo is also available as a jupyter notebook (see demo_pipeline_cnmfE.ipynb)
"""

import logging
import matplotlib.pyplot as plt
import numpy as np
import os
import cv2
from matplotlib.pyplot import savefig

#try:
#    if __IPYTHON__:
#        # this is used for debugging purposes only. allows to reload classes when changed
#        get_ipython().magic('load_ext autoreload')
#        get_ipython().magic('autoreload 2')
#except NameError:
#    pass

import caiman as cm
from caiman.source_extraction import cnmf
from caiman.utils.visualization import inspect_correlation_pnr
from caiman.motion_correction import MotionCorrect
from caiman.source_extraction.cnmf import params as params
from bonsai_funcs import getVideoList

#%%
# Set up the logger; change this if you like.
# You can log to a file using the filename parameter, or make the output more or less
# verbose by setting level to logging.DEBUG, logging.INFO, logging.WARNING, or logging.ERROR

logging.basicConfig(format=
                    "%(relativeCreated)12d [%(filename)s:%(funcName)20s():%(lineno)s]"\
                    "[%(process)d] %(message)s",
                    level=logging.DEBUG)
    # filename="/tmp/caiman.log"

#%%
def caiman_process_session(sessionDir, resultName,
                           downsampleRate = 2, skipHead = 1, skipEnd = 1,
                           tempDir = 'F:\\Caiman_Workfolder\\Movies'):
    pass # For compatibility between running under Spyder and the CLI

# %% start the cluster
    try:
        cm.stop_server()  # stop it if it was running
    except():
        pass

    c, dview, n_processes = cm.cluster.setup_cluster(backend='local',
                                                     n_processes=12,  # number of process to use, if you go out of memory try to reduce this one
                                                     single_thread=False)

    # Clean previous temp data
    if os.path.exists(tempDir):
        tempFiles = [os.path.join(tempDir,f) for f in os.listdir(tempDir)]
        for f in tempFiles:
            os.remove(f)
    else:
        os.mkdir(tempDir)

    results_folder = os.path.join(sessionDir, resultName)
    if not os.path.exists(results_folder):
        os.mkdir(results_folder)
    results_prefix = resultName + '_'

    # Get the list of videos to be processed
    videoLists = getVideoList(sessionDir, fullPathFlag = False)
    videoListsFull = getVideoList(sessionDir, fullPathFlag = True)
    
    for thisList in videoListsFull:
        selectVideoFiles = thisList[skipHead:-skipEnd:]
        inputVideoFile = cv2.VideoCapture(selectVideoFiles[0])
        frame_width = int(inputVideoFile.get(cv2.CAP_PROP_FRAME_WIDTH)/2)
        frame_height = int(inputVideoFile.get(cv2.CAP_PROP_FRAME_HEIGHT)/2)
        frame_rate = int(inputVideoFile.get(cv2.CAP_PROP_FPS))
        fourcc = int(inputVideoFile.get(cv2.CAP_PROP_FOURCC))
        
        inputVideoFile.release()
        
        for f in selectVideoFiles:
            print('Downsampling ' + f)
            inputVideoFile = cv2.VideoCapture(f)
#            outputVideoFile = cv2.VideoWriter(os.path.join(tempDir, f), cv2.VideoWriter_fourcc('M','J','P','G'),
#                                              frame_rate, (frame_width,frame_height))
            outputVideoFile = cv2.VideoWriter(os.path.join(tempDir, os.path.basename(f)), fourcc,
                                              frame_rate, (frame_width,frame_height))
            if (inputVideoFile.isOpened() == False): 
              print("Error opening video stream or file")
             
            while(inputVideoFile.isOpened()):
              ret, frame = inputVideoFile.read()
              if ret == True:
                  outputVideoFile.write(frame[::downsampleRate,::downsampleRate,:])
              else: 
                break
             
            inputVideoFile.release()
            outputVideoFile.release()
            
    rangeList = []
    fnames = []
    for thisList in videoLists:
        selectVideoFiles = thisList[skipHead:-skipEnd:]
        fnames.extend(selectVideoFiles)
        thisListSize = np.shape(thisList)[0]
        rangeList.extend([range(skipHead*1000, (thisListSize-skipEnd)*1000)])

    fnames_temp = [os.path.join(tempDir,f) for f in fnames]    
    

# %% First setup some parameters for motion correction
    # dataset dependent parameters

    filename_reorder = fnames_temp
    fr = 30                          # movie frame rate
    decay_time = 0.4                  # length of a typical transient in seconds

    # motion correction parameters
    motion_correct = True            # flag for motion correction
    pw_rigid = False                 # flag for pw-rigid motion correction

    gSig_filt = (7, 7)   # size of filter, in general gSig (see below),
    #                      change this one if algorithm does not work
    max_shifts = (30, 30)  # maximum allowed rigid shift
    strides = (48, 48)   # start a new patch for pw-rigid motion correction every x pixels
    overlaps = (24, 24)  # overlap between pathes (size of patch strides+overlaps)
    # maximum deviation allowed for patch with respect to rigid shifts
    max_deviation_rigid = 3
    border_nan = 'copy'

    mc_dict = {
        'fnames': fnames_temp,
        'fr': fr,
        'decay_time': decay_time,
        'pw_rigid': pw_rigid,
        'max_shifts': max_shifts,
        'gSig_filt': gSig_filt,
        'strides': strides,
        'overlaps': overlaps,
        'max_deviation_rigid': max_deviation_rigid,
        'border_nan': border_nan
    }

    opts = params.CNMFParams(params_dict=mc_dict)

# %% MOTION CORRECTION
#  The pw_rigid flag set above, determines where to use rigid or pw-rigid
#  motion correction
    if motion_correct:
        # do motion correction rigid
        mc = MotionCorrect(fnames_temp, dview=dview, **opts.get_group('motion'))
        mc.motion_correct(save_movie=True)
        fname_mc = mc.fname_tot_els if pw_rigid else mc.fname_tot_rig
        print(fname_mc)
        if pw_rigid:
            bord_px = np.ceil(np.maximum(np.max(np.abs(mc.x_shifts_els)),
                                         np.max(np.abs(mc.y_shifts_els)))).astype(np.int)
        else:
            bord_px = np.ceil(np.max(np.abs(mc.shifts_rig))).astype(np.int)
            plt.subplot(1, 2, 1); plt.imshow(mc.total_template_rig)  # % plot template
            plt.subplot(1, 2, 2); plt.plot(mc.shifts_rig)  # % plot rigid shifts
            plt.legend(['x shifts', 'y shifts'])
            plt.xlabel('frames')
            plt.ylabel('pixels')

        bord_px = 0 if border_nan is 'copy' else bord_px
        fname_new = cm.save_memmap(fname_mc, base_name='memmap_', order='C',
                                   border_to_0=bord_px)
        for fname in fname_mc:
            os.remove(fname)
    else:  # if no motion correction just memory map the file
        fname_new = cm.save_memmap(filename_reorder, base_name='memmap_',
                                   order='C', border_to_0=0, dview=dview)
    savefig(results_folder + '\\' + results_prefix + 'motion-correct.pdf', bbox_inches='tight')


    # load memory mappable file
    Yr, dims, T = cm.load_memmap(fname_new)
    images = Yr.T.reshape((T,) + dims, order='F')


# %% Parameters for source extraction and deconvolution (CNMF-E algorithm)

    p = 2               # order of the autoregressive system
    K = None            # upper bound on number of components per patch, in general None for 1p data
    gSig = (2, 2)       # gaussian width of a 2D gaussian kernel, which approximates a neuron
    gSiz = (9, 9)     # average diameter of a neuron, in general 4*gSig+1
    Ain = None          # possibility to seed with predetermined binary masks
    merge_thresh = .7   # merging threshold, max correlation allowed #0.7
    rf = 40             # half-size of the patches in pixels. e.g., if rf=40, patches are 80x80
    stride_cnmf = 15    # amount of overlap between the patches in pixels
    #                     (keep it at least large as gSiz, i.e 4 times the neuron size gSig)
    tsub = 2            # downsampling factor in time for initialization,
    #                     increase if you have memory problems
    ssub = 1            # downsampling factor in space for initialization,
    #                     increase if you have memory problems
    #                     you can pass them here asl boolean vectors
    low_rank_background = None  # None leaves background of each patch intact,
    #                     True performs global low-rank approximation if gnb>0
    gnb = 0             # number of background components (rank) if positive,
    #                     else exact ring model with following settings
    #                         gnb= 0: Return background as b and W
    #                         gnb=-1: Return full rank background B
    #                         gnb<-1: Don't return background
    nb_patch = 0        # number of background components (rank) per patch if gnb>0,
    #                     else it is set automatically
    min_corr = 0.8       # min peak value from correlation image #0.8
    min_pnr = 10        # min peak to noise ration from PNR image #10
    ssub_B = 2          # additional downsampling factor in space for background
    ring_size_factor = 1.4  # radius of ring is gSiz*ring_size_factor

    params_dict={'dims': dims,
                 'method_init': 'corr_pnr',  # use this for 1 photon
                 'K': K,
                 'gSig': gSig,
                 'gSiz': gSiz,
                 'merge_thresh': merge_thresh,
                 'p': p,
                 'tsub': tsub,
                 'ssub': ssub,
                 'rf': rf,
                 'stride': stride_cnmf,
                 'only_init': True,    # set it to True to run CNMF-E
                 'nb': gnb,
                 'nb_patch': nb_patch,
                 'method_deconvolution': 'oasis',       # could use 'cvxpy' alternatively
                 'low_rank_background': low_rank_background,
                 'update_background_components': True,  # sometimes setting to False improve the results
                 'min_corr': min_corr,
                 'min_pnr': min_pnr,
                 'normalize_init': False,               # just leave as is
                 'center_psf': True,                    # leave as is for 1 photon
                 'ssub_B': ssub_B,
                 'ring_size_factor': ring_size_factor,
                 'del_duplicates': True,                # whether to remove duplicates from initialization
                 'border_pix': bord_px}

    opts.change_params(params_dict=params_dict)                # number of pixels to not consider in the borders)

# %% compute some summary images (correlation and peak to noise)
    # change swap dim if output looks weird, it is a problem with tiffile
    cn_filter, pnr = cm.summary_images.correlation_pnr(images, gSig=gSig[0], swap_dim=False)
    # inspect the summary images and set the parameters
    inspect_correlation_pnr(cn_filter, pnr)
    savefig(results_folder + '\\' + results_prefix + 'corr-pnr.pdf', bbox_inches='tight')
    # print parameters set above, modify them if necessary based on summary images
    print(min_corr) # min correlation of peak (from correlation image)
    print(min_pnr)  # min peak to noise ratio


# %% RUN CNMF ON PATCHES
    cnm = cnmf.CNMF(n_processes=n_processes, dview=dview, Ain=Ain, params=opts)
    cnm.fit(images)

# %% ALTERNATE WAY TO RUN THE PIPELINE AT ONCE
    #   you can also perform the motion correction plus cnmf fitting steps
    #   simultaneously after defining your parameters object using
#    cnm1 = cnmf.CNMF(n_processes, params=opts, dview=dview)
#    cnm1.fit_file(motion_correct=True)


# %% DISCARD LOW QUALITY COMPONENTS
    min_SNR = 4           # adaptive way to set threshold on the transient size #2.5
    r_values_min = 0.9    # threshold on space consistency (if you lower more components #0.85
    #                        will be accepted, potentially with worst quality)
    qual_dict =  {'min_SNR': min_SNR,
                               'rval_thr': r_values_min,
                               'use_cnn': False}
    
    cnm.params.set('quality', qual_dict)
    cnm.estimates.evaluate_components(images, cnm.params, dview=dview)

    print(' ***** ')
    print('Number of total components: ', len(cnm.estimates.C))
    print('Number of accepted components: ', len(cnm.estimates.idx_components))


    A = cnm.estimates.A.todense()
    C = cnm.estimates.C
    S = cnm.estimates.S
    b = cnm.estimates.b
    f = cnm.estimates.f
    YrA = cnm.estimates.YrA
    sn = cnm.estimates.sn
    idx_components = cnm.estimates.idx_components
    idx_components_bad = cnm.estimates.idx_components_bad

## %% PLOT COMPONENTS
#    cnm.dims = dims
#    cnm.estimates.plot_contours(img=cn_filter, idx=cnm.estimates.idx_components)
#    savefig(results_folder + results_prefix + 'contours.pdf', bbox_inches='tight')


    # PLOT COMPONENTS
    plt.figure(figsize=(15*3,8*3));
    plt.subplot(121);
    crd = cm.utils.visualization.plot_contours(A[:,idx_components], cn_filter, thr=.8, vmax=0.95)
    plt.title('Contour plots of accepted components', fontsize=12)
    
    plt.tick_params(
        axis='y',        # changes apply to the x-axis
        which='both',    # both major and minor ticks are affected
        left='off',      # ticks along the bottom edge are off
        right='off',
        labelleft='off') # ticks along the top edge are off
    plt.tick_params(
        axis='x',        # changes apply to the x-axis
        which='both',    # both major and minor ticks are affected
        top='off',       # ticks along the bottom edge are off
        bottom='off',
        labelleft='off') # ticks along the top edge are off
    
    plt.subplot(122); 
    crd = cm.utils.visualization.plot_contours(A[:,idx_components_bad], cn_filter, thr=.8, vmax=0.95)
    plt.title('Contour plots of rejected components', fontsize=12)
    plt.tick_params(
        axis='y',        # changes apply to the x-axis
        which='both',    # both major and minor ticks are affected
        left='off',      # ticks along the bottom edge are off
        right='off',
        labelleft='off') # ticks along the top edge are off
    plt.tick_params(
        axis='x',        # changes apply to the x-axis
        which='both',    # both major and minor ticks are affected
        top='off',       # ticks along the bottom edge are off
        bottom='off',
        labelleft='off') # ticks along the top edge are off
    
    savefig(results_folder + '\\' + results_prefix + 'contours.pdf', bbox_inches='tight')

    plt.close('all')
    

    #%% SAVE RESULTS
    # A: Vectorized outline of the contours of cells
    # C: matrix of temporal components (K x T)
    # S: matrix of merged deconvolved activity (spikes) (K x T)
    # b:  baseline for fluorescence trace for each column in A (I think...)
    # f: vector of temporal background (length T)
    # YrA: matrix of spatial component filtered raw data, after all contributions have been removed. YrA corresponds to the residual trace for each component and is used for faster plotting (K x T)
    # sn: noise level for each column in A

    np.savez(results_folder + '\\' + results_prefix + 'results.npz', 
             mc_dict = mc_dict,
             params_dict = params_dict, 
             qual_dict = qual_dict,
             A=A, 
             C=C,
             S=S,
             b=b, 
             f=f, 
             YrA=YrA, 
             sn=sn, 
             dims = dims, 
             idx_components=idx_components, 
             idx_components_bad=idx_components_bad,
             rangeList = rangeList)
    
# %% STOP SERVER
    cm.stop_server(dview=dview)
