import ctypes
ll = ctypes.cdll.LoadLibrary
lib = ll("./libstd_dev.so")
sum =lib.add(1, 3) 
print("sum: ", sum)