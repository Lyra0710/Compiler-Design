def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence

count = 10
fib_sequence = fibonacci(count)
print(f"The first {count} numbers in the Fibonacci sequence are: {fib_sequence}")
