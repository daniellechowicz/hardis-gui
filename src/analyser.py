import itertools
import math
import numpy as np
from scipy.signal import find_peaks


class Analyser(object):
    def __init__(self, fs, cutting_speed):
        self.fs = fs
        self.cutting_speed = cutting_speed

    def process_scanner(self, data):
        # Specify cutting duration according to applied cutting speed and sampling rate
        cutting_duration = int(0.1 * self.fs / self.cutting_speed)

        # Find a window corresponding to the cutting process
        values = []
        for i in range(0, len(data)):
            try:
                value = np.mean(data[i : i + cutting_duration])
                values.append(value)
            except Exception as e:  # in case if i + cutting_duration > len(data)
                print(e)

        start = values.index(max(values))
        finish = start + cutting_duration

        return start, finish