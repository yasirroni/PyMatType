from numpy import ndarray, atleast_2d, asarray, indices

class array(ndarray):
    def __new__(cls, val):
        val = atleast_2d(asarray(val, dtype=object))

        obj = asarray(val).view(cls)
        
        # Add the new attribute to the created instance here:
        obj._matlab_array_index = None # _matlab_array_index is lazyly created

        # Finally, we must return the newly created object:
        return obj

    def __array_finalize__(self, obj):
        # see InfoArray.__array_finalize__ for comments
        if obj is None:
            return

        self._matlab_array_index = getattr(obj,'_matlab_array_index', None)

    def __getitem__(self, key):
        if isinstance(key, int) or isinstance(key, float):
            if self._matlab_array_index is None:
                self._make_matlab_array_index()
            key = tuple(self._matlab_array_index[int(key)])
        
        return super().__getitem__(key)
    
    def _make_matlab_array_index(self):
        idx = indices(self.shape).reshape((self.ndim, -1)).T
        idx = idx[idx[:,0].argsort()]
        for i in range(1,len(self.shape),1):
            idx = idx[idx[:,i].argsort(kind='mergesort')]

        self._matlab_array_index = idx

