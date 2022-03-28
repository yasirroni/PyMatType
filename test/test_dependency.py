try:
    import numpy
    NUMPY_EXISTS = True
except ImportError:
    NUMPY_EXISTS = False

class TestDependency:
    @classmethod
    def test_import_numpy():
        assert NUMPY_EXISTS is True
