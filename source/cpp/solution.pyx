from libcpp.vector cimport vector

cdef extern from "solution.hpp":
    cdef cppclass Solution:
        Solution() except + 
        int jump(vector[int]& nums)

cdef class cppSolution:
    cdef Solution *ptr
    def __cinit__(self): self.ptr = new Solution()
    def __dealloc__(self): del self.ptr

    def jump(self, nums):
        cdef vector[int] array
        cdef int num

        for num in nums: array.push_back(num)
        result = self.ptr.jump(array)
        return result