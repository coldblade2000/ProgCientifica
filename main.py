# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
##
import numpy as np

a = [i for i in range(0,20)]
np_array = np.array(a)
print(np_array)

np.zeros((4,2))
np.ones((5,2))
##
n= 17
bitfield = list(bin(n)[2:])

bitfield[-1] = int(bitfield[-1]) + 1

print(bitfield)

