import pytest

from myapp.mymodule.funcs import *
# Daniel Allen 
# Student Number: 100624358

@pytest.mark.difficult_operation
def test_multiply():
    assert multiply(1, 20) == 58
