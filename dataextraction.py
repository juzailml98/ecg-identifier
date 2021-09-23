
import glob
import numpy as np
def record_collector():
    atr_file_path=glob.glob('dataset/*.atr')
    return atr_file_path

print(record_collector())
