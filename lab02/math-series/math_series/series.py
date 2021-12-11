

def fibonacci(n):
    """
    The Fibonacci Series is a numeric series starting with the integers 0 and 1. 
    In this series, the next integer is determined by summing the previous two.

    Args:
        n (int): The function will return the nth number in the fibonacci sequence
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def lucas(n):
    """
    The Lucas Numbers are a related series of integers that start with the values 2 and 1 rather than 0 and 1.

    Args:
        n (int): The function will return the nth number in the lucas sequence
    """   
    if n < 0:
        return 0 
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)

def sum_series(n, first_num=0, second_num=1):
    """
    Calling this function with no optional parameters will produce numbers from the fibonacci series.
    Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers. 
    Other values for the optional parameters will produce other series. 

    Args:
        n (int): The function will return the nth number in the sequence.
        first_num (int, optional): First number in the sequence. Defaults to 0.
        second_num (int, optional): Second number in the sequence. Defaults to 1.
    """
    if n < 0:
        return 0
    elif n == 0:
        return first_num
    elif n == 1:
        return second_num  
    else:
        return sum_series(n - 1, first_num, second_num) + sum_series(n - 2, first_num, second_num)
