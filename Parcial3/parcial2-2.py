
import numpy as np
import struct as st
import random
nums = []

for i in range(0, 200):
    nums.append(random.randrange(-10, 10))

file = open("FileBinInt16.bin", "wb+")
packed = st.pack("f" * len(nums), *nums)
print(len(packed))
file.write(packed)
file.close()
