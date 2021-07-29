
def fibonacci(n):
    """
    this is function Work as fibonacci it take The number and give you the nth of the fibonacci's Series 
    """

    value1 = 0
    value2 = 1
    nth = 0
    conter = 2
    if n == 0:
        return 0
    if n == 1:
        return 1

    while n:
        conter += 1
        nth = value1+value2
        value1 = value2
        value2 = nth
        if n == conter:
            return(nth)


print(fibonacci(7))


def lucas(n):
    """
    this is function Work as lucas it take The number and give you the nth of the lucas's Series 
    """
    nth = 0
    value1 = 2
    value2 = 1
    counter = 2

    if n == 0:
        nth = 2
        return 2
    elif n == 1:
        nth = 1

        return 1

    else:

        while n:

            nth = value1+value2
            value1 = value2
            value2 = nth
            counter += 1
            if n == counter:
                return nth


def sum_series(n, value1=0, value2=1):

    if n < 0:
        return " +ve Number "
    elif n == 0:
        return value1
    elif n == 1:
        return value2
    else:
        return(sum_series(n-1, value1, value2)+sum_series(n-2, value1, value2))
