import pytest

from myapp.mymodule.funcs import *
# Daniel Allen 


@pytest.mark.difficult_operation
def test_multiply():
    assert multiply(2, 29) == 58
