# https://blog.csdn.net/weixin_30532973/article/details/97703470
# python
import math
import time
import numpy as np
import cyStdDev
 
def pyStdDev(a):
    mean = sum(a) / len(a)
    return math.sqrt((sum(((x - mean)**2 for x in a)) / len(a)))


def npStdDev(a):
    return np.std(a)

def test():
    num = 10000
    a1 = [float(v) for v in range(num)]
    t_py = time.time()
    py_result = pyStdDev(a1)
    print("t_py: ", time.time()-t_py)
    print("t_py result: ", py_result)

    # ------------------------
    print("*"*30)
    a2 = np.arange(num)
    t_np = time.time()
    np_result = npStdDev(a2)
    print("t_np: ", time.time()-t_np)
    print("t_np result: ", np_result)

    # ------------------------
    print("*"*30)
    a = np.arange(num)
    t_cy = time.time()
    cy_result = cyStdDev.cyStdDev(a)
    print("t_cy: ", time.time()-t_cy)
    print("cy result: ", cy_result)

    # -----------------------
    print("*"*30)
    a3 = np.arange(num)
    t_cy_np = time.time()
    cy_np_result = cyStdDev.npStdDev(a3)
    print("t_cy_np: ", time.time()-t_cy_np)
    print("cy_np result: ", cy_np_result)

    # ------------------------
    print("*"*30)
    # a4 = np.arange(1e6)
    a4 = np.arange(num)
    t_cy_opt_np = time.time()
    print("t_cy_opt_np: ", time.time()-t_cy_opt_np)
    print("cy_opt_np result: ", cyStdDev.cyStdDev(a4))

    # ------------------------
    print("*"*30)
    # a5 = np.arange(1e4) #np.arange(num)
    a5 = np.arange(float(num))
    print("dtype: ",str(a5.dtype))
    t_c = time.time()
    c_result = cyStdDev.cStdDev(a5)
    print("t_c: ", time.time()-t_c)
    print("c result: ", c_result)

    res = cyStdDev.shannon_entropy_v2(np.array([10.0, 20]))
    print("res: ", res)

if __name__=="__main__":
    test()

# fatal error: numpy/arrayobject.h: 没有那个文件或目录--> sudo apt-get install python-numpy