# -*- coding: utf-8 -*-

"""
Created on Fri May 19 11:43:04 2023

@author: Luca
"""
import pandas as pd
import os

class tms_data:
    
    def __init__(self, path: str, timestamp: str):
        
        # data path
        self.path = path
        
        # Timestamp appearing on the filenames
        self.timestamp = timestamp
        
        self.data = {}
        self._filetype = [
                        # =============================================================================
                        # -.raw the raw channel measurement length from the Etalon multiline server.
                        # -.etalon the Etalon corrected channel length data.
                        # -.ciddor our own corrected channel length data (with LBT weather telemetry).
                        # =============================================================================
                          '.raw',
                          '.etalon',
                          '.ciddor',
                        # the calculated pose data (i.e., x,y,z,rx,ry,rz).
                          '.pose.dx',
                          '.pose.sx',
                        # =============================================================================
                        # the calculated standard deviation on each channel. 
                        # The standard deviation is currently calculated on three most recent channel 
                        # measurements
                        # at each given timestamp. The unit is in micron.
                        # =============================================================================
                          'stdev',
                        # =============================================================================
                        # the channel filtering based on standard deviation for each vector. 
                        # Basically if a channel's value is 0, then it is not filtered; 
                        # if instead a channel has 1, then it is being filtered because of exceeding
                        # the standard deviation threshold.
                        # For convenience, the first data row in the file is a summation of
                        # each column (i.e., how many times each channel has been filtered by standard deviation).
                        # =============================================================================
                          'stdev.filter',
                          'stdev.filer.dx',
                          'stdev.filter.sx',
                        # =============================================================================
                        # the intentional exclusion of particular channels. 
                        # If a channel in a vector is 0, then it is not excluded intentionally; 
                        # if a channel has value 1 in its vector, then it is being dropped intentionally. 
                        # For convenience the first data row in the file calculates the summation of each column
                        # (i.e., total excluded times for each channel).
                        # =============================================================================
                          '.drop',
                        # =============================================================================
                        # these are timestamps when a reference is made. 
                        # You can cross reference these timestamps in other files to find out informations
                        # on the references 
                        # (e.g., reference the tms.raw file to find out the raw values and
                        # the tms.pose.sx and tms.pose.dx to find out the reference pose calculated).
                        # =============================================================================
                          '.ref.dx',
                          '.ref.sx',
                        # Weather telemetry
                          '.weather.lbt',
                        # =============================================================================
                        # the final TMS correction vectors computed
                        # (the ones actually sent to the telescope).
                        # =============================================================================
                          'correction.dx',
                          'correction.sx',
                          'thermalz4.dx',
                          'thermalz4.sx']
        for row, di, files in os.walk(self.path):
            for f in files:
                if f.endswith(tuple(self._filetype)):
                    self.data[f.split('.', maxsplit=1)[1]] = pd.read_table(os.path.join(row, f),
                                                     sep = ',')        
        for atr in self.data:
            if len(self.data[atr]) == 0:
                print(f'{atr} file not found')