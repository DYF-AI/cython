import math

def cyStdDev(a):
    m = a.mean()
    w = a - m
    wSq = w**2
    return math.sqrt(wSq.mean())

import numpy as np
def npStdDev(a):
    return np.std(a)

import torch
def torchStdDev(a):
    return torch.std(a)


cimport numpy as cnp
from libc.math cimport log as clog

def shannon_entropy_v2(cnp.ndarray[double] p_x):
    cdef double res = 0.0
    cdef int n = p_x.shape[0]
    cdef int i
    for i in range(n):
        res += p_x[i] * clog(p_x[i])
    return -res

cdef extern from "math.h":
    double sqrt(double m)

from numpy cimport ndarray
cimport numpy as np
cimport cython

@cython.boundscheck(False)
def cyOptStdDev(ndarray[np.float64_t, ndim=1] a not None):
    cdef Py_ssize_t i
    cdef Py_ssize_t n = a.shape[0]
    cdef double m = 0.0
    for i in range(n):
        m += a[i]
    m /= n
    cdef double v = 0.0
    for i in range(n):
        v += (a[i] - m)**2
    return sqrt(v / n)

cdef extern from "std_dev.c":
    double std_dev(double *arr, size_t siz)

def cStdDev(ndarray[np.float64_t, ndim=1] a not None):
    return std_dev(<double*> a.data, a.size)