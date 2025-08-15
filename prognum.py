def fibonacci_prog(num):
    if num <= 2:
        return 1

    return fibonacci_prog(num - 1) + fibonacci_prog(num - 2)
