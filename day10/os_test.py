import os
import sys
def test_os():
    print(os.listdir())
    print("返回当前路径：", os.path.realpath('os_test.py'))
    print("返回当前路径：", os.path.abspath('os_test.py'))
    print("路径 c:\develop\code是否存在", os.path.exists('c:\develop\\test1'))
    if not os.path.exists('c:\develop\\test1'):
        os.makedirs('c:\\develop\\test1')

    # print(dir(os))
    print(dir(sys.path))
