import os
import sys
import pandas as pd
#import numpy as np
#import sklearn
#from sklearn import svm
#import dask.dataframe as dd
#from matplotlib import pyplot as plt 

#import winsound
#freq = 100
#dur = 50


class csvcombiner:

    @staticmethod
    def check_path(argv):

        folder_files = argv[1:]

        for i in folder_files:
            if not os.path.exists(i):
                print(f"{i} does not exists!")
                return False

        return True

    def combine_csv(self, argv: tuple):
        chunksize = 100000
        chunk_list = []

        if self.check_path(argv):
            folder_files = argv[1:]

            for i in folder_files:
			#for j in dd.read_csv(i, chunksize=chunksize):
                for j in pd.read_csv(i, chunksize=chunksize):
                    filename = os.path.basename(i) 
                    j['filename'] = filename
                    chunk_list.append(j)
            header = True
	    #print(f"New chucklist after first csv: {chuck_list}")
            for j in chunk_list:
                print(j.to_csv(index=False, header=header, line_terminator='\n', chunksize=chunksize), end='')
            header = True
        else:
            return
	   #print(f"New chucklist after second csv: {chuck_list}")

    '''
    for i in range(0, 10):    
    winsound.Beep(freq, dur)    
    freq+= 100
    dur+= 50
    '''


def main():
    csv_combiner = csvcombiner()
    csv_combiner.combine_csv(sys.argv)

if __name__ == '__main__':
    main()
