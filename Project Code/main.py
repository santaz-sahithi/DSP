"""
Main execution file

Copyright 2020 by Blagoj Hristov

See the LICENSE file for the licensing associated with this software.

Author:
  Blagoj Hristov, March 2020

"""

import os
import sys
import numpy as np
from feature_extraction.spectral import generate_mfcc
from refactoring.transcript import index_transcripts
from refactoring.files import rename_files
from preprocessing.audio import resample_audio
from utils.utils import load_mfcc

if __name__ == '__main__':

    data_path = 'F:\\Speech_Recognition_Macedonian\\Database\\train'
    rate = 16000
    coeff = 13

    batch_features = load_mfcc(data_path + os.sep + '1' + os.sep + '000000')

    # rename_files(path=data_path, verbose=True)

    # generate_mfcc(path=data_path, sampling_rate=rate, num_coeff=coeff, verbose=True)
