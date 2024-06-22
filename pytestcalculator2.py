from pytestcalculator1 import square
import pytest
def test_positive():
    assert square(2)==4
    assert square(3)==9

def test_negative():
    assert square(-2)==4
    assert square(-3)==9

def test_zero():
    assert square(0)==0

def test_str():
    with pytest.raises(TypeError):
        square('cat')
    #pytest <filename>.py instead than python <filename>.py to test  your code.

#square function in the last file is the biggest prove it works, you can make it return n + n and see the output.
