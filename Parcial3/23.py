import numpy as np
import struct as st
fil = open("FileBinInt16.bin", "rb")
Data = fil.read()
fil.close()
DataO = np.int16(st.unpack("d"*int(len(Data)/8), Data))
print(len(DataO))
