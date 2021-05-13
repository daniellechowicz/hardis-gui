from scipy.signal import butter, hilbert, lfilter
import analyser
import numpy as np


class Filter(object):
    def __init__(self, fs):
        self.fs = fs

    def butter_lowpass_filter(self, data, cut_off=1500, order=5):
        nyq = 0.5 * self.fs
        normal_cutoff = cut_off / nyq
        b, a = butter(order, normal_cutoff, btype="low", analog=False)
        data = self.offset(data)
        y = lfilter(b, a, data)

        return y

    def offset(self, data):
        # Mean value out of 10 000 first samples
        offset_Y = np.mean(data[0:10000])

        if offset_Y > 0:
            data -= abs(offset_Y)
        else:
            data += abs(offset_Y)

        return data
