from pytestcalculator1 import square
def test_square():
    assert square(2)==4
    assert square(3)==9
    assert square(-2)==4
    assert square(-3)==9
    assert square(0)==0
    #pytest <filename>.py instead than python <filename>.py to test  your code.