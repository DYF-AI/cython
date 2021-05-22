import ctypes
ll = ctypes.cdll.LoadLibrary
lib = ll("./libpycall.so")
sum =lib.add(1, 3) 
print("sum: ", sum)