def print_fibonacci(length):
    if length == 0:
        return []
    elif length == 1:
        return [0]
    elif length == 2:
        return [0, 1]
    else:
        first, second = 0, 1
        fib_sequence = []
        for i in range(length):
            fib_sequence.append(first)
            first, second = second, first + second
        return fib_sequence

# Test the function
print(print_fibonacci(10))