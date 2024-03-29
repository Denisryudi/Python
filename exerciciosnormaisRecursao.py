
def fatorial(n):
    if n <= 1:
        return 1
    else:
        return n * fatorial(n-1)

def test_fatorial():
    assert fatorial(0) == 1
    assert fatorial(1) == 1
    assert fatorial(2) == 2
    assert fatorial(3) == 6
    assert fatorial(4) == 24
    assert fatorial(5) == 120