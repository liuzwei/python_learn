import numpy as np

def test_np():
    # 顶一个一的numpy数组
    print("-----------arrya1-----------")
    array1 = np.array([1, 2, 3, 4, 5])
    print(array1) 
    print("array1的类型：", type(array1))
    print("array1的形状：", array1.shape)
    print("array1的维度：", array1.ndim)
    print("array1的大小：", array1.size)
    print("array1的数据类型：", array1.dtype)
    print("array1的元素字节大小：", array1.itemsize)
    print("array1的内存地址：", array1.data)

    print()
    print("-----------arrya2-----------")
    array2 = np.array([(1,2,3,4,5,6),(1,3,5,7,9,11)], dtype=complex)
    print(array2)

    print()
    print("-----------zeros-----------")
    zeros = np.zeros((4,5))
    print(zeros)

    print()
    print("-----------ones-----------")
    ones = np.ones((4,5))
    print(ones)

    print()
    print("-----------empty-----------")
    empty = np.empty((3,5))
    print(empty)

    print()
    print("-----------arrange-----------")
    arrange = np.arange(0, 100, 2.5)
    print(arrange)
    
    print()
    print("-----------linspace-----------")
    linspace = np.linspace(0, 3, 9)
    print(linspace)

    print(np.arange(0, 2000).reshape(200, 10))

    print()
    print("-----------basic operation-----------")
    ar1 = np.array([10, 20, 30, 40])
    ar2 = np.arange(4)
    print("ar1+ar2:", ar1+ar2)
    print("ar1-ar2:", ar1-ar2)
    print("ar2的平方:", ar2**2)
    print("ar1*ar2:", ar1*ar2)
    print("ar1+=3:", ar1+3)
    print("ar1的和", ar1.sum())

    print()
    print("-----------sum-----------")
    arsum = np.arange(20).reshape(4,5)
    print("arsum:", arsum)
    print("arsum:", arsum.sum())
    print("arsum:", arsum.sum(axis=0))
    print("arsum:", arsum.sum(axis=1))

    print()
    print("-----------Universal Function-----------")
    uar = np.array([1, 4, 9, 16])
    print("uar sqrt:", np.sqrt(uar))
    print("uar exp:", np.exp(uar))

    print()
    print("-----------reshape-----------")
    r = np.arange(20).reshape(4,5, order='F')
    print("r is 4x5:\n",r)
    r = np.arange(20).reshape(4, 5, order='C')
    print("r is 4x5:\n",r)

    print()
    print("-----------narray.flat-----------")
    r = np.arange(20).reshape(4,5)
    for a in r.flat:
        # 迭代打印每一个元素
        print(a)


