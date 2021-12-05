import numpy as np
from sympy import *
import matplotlib.pyplot as plt
import struct as st
from scipy.interpolate import CubicSpline

def f1(x1, x2):
    return x1 ** 2 + x2 **2 - 1

def f2(x1, x2):
    return x1**2 - x2

