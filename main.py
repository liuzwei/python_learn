from day09.day09_1 import generateStudentInfo
from day10.os_test import test_os
from numpy_test.np import test_np
from matplotlib_test.matplotlib import test_matplotlib
import numpy as np

def main():
    # day 09
    # generateStudentInfo()
    # test_os()
    # Numpy
    # test_np()
    # matplotlib
    test_matplotlib()
    s = [[0 for i in range(10)] for i in range(10)]
    
    print(np.array(s))
    
# main方法
if __name__ == '__main__':
    main()