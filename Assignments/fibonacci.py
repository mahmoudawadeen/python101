def fib(fibonacci_limit):
    fib_1 = 1
    fib_2 = 1
    for i in range(0, fibonacci_limit + 1):
        if i == 1 or i == 0:
            print("fib of", i, "is", 1)
            yield 1
        else:
            result = fib_1 + fib_2
            fib_2 = fib_1
            fib_1 = result
            print("fib of", i, "is", result)
            yield result


x = fib(4)
next(x)
next(x)
next(x)
next(x)
next(x)
