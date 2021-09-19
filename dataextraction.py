print("hello world")
import glob
def record_collector():
    atr_file_path=glob.glob('dataset/*.atr')
    #print(atr_file_path)
    #atr_file_path = [path[:-4] for path in atr_file_path]
    #atr_file_path.sort()
    return atr_file_path

print(record_collector())
