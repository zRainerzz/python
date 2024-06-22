from heloooo import hello

def test_default():
    assert hello()=="Hello, World"
def test_argument():
    for name in ['Hermone', 'Tesla', 'Sasuke']:
        assert hello(name)== f"Hello, {name}"