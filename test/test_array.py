from numpy import indices, arange # for create data
from numpy import array_equal # for test

from pymattype import array

class TestArray  :
    @classmethod
    def setup_class(cls):
        cls.nval = 24
        cls.shape = (3,2,4)
        cls.ndim = len(cls.shape)

        idx = indices(cls.shape).reshape((cls.ndim, -1)).T
        idx = idx[idx[:,0].argsort()]
        for i in range(1,len(cls.shape),1):
            idx = idx[idx[:,i].argsort(kind='mergesort')]
        cls.matlab_array_index = idx  

        cls.narr = arange(cls.nval).reshape(cls.shape)
        cls.A = array(cls.narr)
        # print('array:')
        # print(A)      

    def test_dimension(self):
        # atleast2d
        assert len(self.A.shape) >= 2

    def test_using_int_key(self):
        # print('using int key:')
        for i in range(24):
            # print(self.A[i])
            # print(self.matlab_array_index[i])
            # print(self.narr[tuple(self.matlab_array_index[i])])
            assert array_equal(self.A[i], self.narr[tuple(self.matlab_array_index[i])])

    def test_using_float_key(self):
        # print('using float key:')
        for i in range(24):
            i_float = i/1
            # print(self.A[i_float])
            # print(self.A._matlab_array_index[i])
            assert array_equal(self.A[i_float], self.narr[tuple(self.matlab_array_index[i])])

    # tuple_key = (1,1,1)
    # print(f'using tuple key {tuple_key}:')
    # print(A[tuple_key])

    # slice_key = tuple([1,slice(0,2,1),2])
    # print(f'using tuple of slice key {slice_key}:')
    # print(A[slice_key])

    # print(f'using direct slice key "[1,:,2]":')
    # print(A[1,:,2])

    # list_key = [1]
    # print(f'using list key {list_key}:')
    # print(A[list_key])

    # print('type key:')
    # print(type(A))

if __name__ == "__main__":
    a = TestArray()
    a.setup_class()
    a.test_using_int_key()
    a.test_using_float_key()
