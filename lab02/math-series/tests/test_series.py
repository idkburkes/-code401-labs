from math_series.series import fibonacci, lucas, sum_series

# tests for fibonacci()
def test_fibonacci_n_equals_0():
    expected = 0
    actual = fibonacci(0)
    assert expected == actual

def test_fibonacci_n_equals_1():
    expected = 1
    actual = fibonacci(1)
    assert expected == actual

def test_fibonacci_n_equals_2():
    expected = 1
    actual = fibonacci(2)
    assert expected == actual

def test_fibonacci_n_equals_4():
    expected = 3
    actual = fibonacci(4)
    assert expected == actual

def test_fibonacci_n_equals_7():
    expected = 13
    actual = fibonacci(7)
    assert expected == actual

def test_fibonacci_n_is_negative():
    expected = 0
    actual = fibonacci(-10)
    assert expected == actual


# Tests for lucas()
def test_lucas_n_equals_0():
    expected = 2
    actual = lucas(0)
    assert expected == actual

def test_lucas_n_equals_1():
    expected = 1
    actual = lucas(1)
    assert expected == actual

def test_lucas_n_equals_2():
    expected = 3
    actual = lucas(2)
    assert expected == actual

def test_lucas_n_equals_4():
    expected = 7
    actual = lucas(4)
    assert expected == actual

def test_lucas_n_equals_7():
    expected = 29
    actual = lucas(7)
    assert expected == actual

def test_lucas_n_is_negative():
    expected = 0
    actual = lucas(-100)
    assert expected == actual

# Tests for sum_series() 


def test_sum_series_with_1_arg():
    expected = 3
    actual = sum_series(4)
    assert expected == actual

def test_sum_series_with_lucas_args():
    expected = 29
    actual = sum_series(7,2,1)
    assert expected == actual

# 5, 1, 6, 7, 13, 20, 33
def test_sum_series_with_2_args():
    expected = 13
    actual = sum_series(4,5)
    assert expected == actual
    
# 2, 7, 9, 16, 25, 41, 66
def test_sum_series_with_3_args():
    expected = 41
    actual = sum_series(5,2,7)
    assert expected == actual